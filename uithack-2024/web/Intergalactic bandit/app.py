import os, time
import flask
from flask_sock import Sock
from simple_websocket.ws import ConnectionClosed

import uuid
import random, secrets
from argon2 import PasswordHasher
from json import JSONDecodeError

# logging
import logging, logging.config, logging.handlers
from logging import DEBUG, INFO
from logging.config import dictConfig
from werkzeug.middleware.proxy_fix import ProxyFix

APP_NAME = "UiTHack24-bandit"

os.makedirs("log", exist_ok=True)  # system logging
os.makedirs("logs", exist_ok=True)  # session/user logging

dictConfig(
    {
        "version": 1,
        "formatters": {
            "verbose": {
                "format": "%(asctime)s %(levelname)s %(name)s:%(lineno)d | %(message)s %(exc_info)s",
                "datefmt": "%Y-%m-%dT%H:%M:%S%z",
            },
            "default": {
                "format": "%(asctime)s %(levelname)s %(name)s: %(message)s",
                "datefmt": "%Y-%m-%dT%H:%M:%S",
            },
            "simple": {
                "format": "%(asctime)s %(levelname)s %(message)s",
                "datefmt": "%H:%M:%S%",
            },
            "plain": {"format": "%(message)s"},
        },
        "handlers": {
            "stdout": {
                "class": "logging.StreamHandler",
                "level": "WARNING",
                "formatter": "simple",
                "stream": "ext://sys.stdout",
            },
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "INFO",
                "formatter": "verbose",
                "filename": f"log/{APP_NAME}.log",
                "maxBytes": 1024**2 * 20,  # 20MB
                "backupCount": 5,
            },
        },
        "loggers": {APP_NAME: {"level": "INFO", "handlers": ["stdout", "file"]}},
    }
)


# init flask
app = flask.Flask(APP_NAME, static_folder="static_files", template_folder="templates")
app.secret_key = secrets.token_bytes(32)
sock = Sock(app)
# enable this for reverse proxy support
# src: https://flask.palletsprojects.com/en/3.0.x/deploying/proxy_fix/
# app.wsgi_app = ProxyFix(
#     app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
# )


def verify_admin(pswd: str) -> bool:
    if len(pswd) == 0:
        return False

    p = bytearray(pswd, "utf-8")
    x = bytearray("*" * len(pswd), "utf-8")
    for i in range(len(pswd)):
        x[i] = (p[i] ^ i) ^ x[i]

    return x == b"B^F]K]\x1e"


def verify_knowledge(pswd: str) -> bool:
    ph = PasswordHasher()
    print("here", pswd)
    with open("pswd.txt", "r") as f:
        return ph.verify(f.read(), pswd)
    return False


## Webserver ##

START_COINS = 200
SPIN_COST = 20
PAYOUT_MULTIPLIER = 5
FLAG_PRICE = 10000
LOG_KEEP_TIME = 60 * 5  # value in seconds
WS_TIMEOUT = 60 * 5  # value in seconds


@app.route("/")
@app.route("/index.html")
def index():
    return flask.render_template("index.html", name="index.html", )


@app.route("/log/<uuid:log_id>", methods=["GET"])
@app.route("/logs/<uuid:log_id>", methods=["GET"])
def log(log_id):
    try:
        with open(f"logs/{log_id}.log", "r") as log_file:
            log_content = log_file.read()
            return flask.Response(log_content, mimetype="text/plain")
    except FileNotFoundError:
        return flask.abort(404)


@app.route("/favicon.ico", defaults={"path": "coin.png"}, methods=["GET"])
@app.route("/<path:path>", methods=["GET"])
def static_files(path: str):
    return flask.send_from_directory("static", path)


@sock.route("/ws")
def connect(ws):
    addr = repr(ws.sock).split("=")[-1][:-1]
    session_id = uuid.uuid4()
    session = {
        "id": session_id.__str__(),
        "addr": addr,
        "coins": START_COINS,
    }

    # create a session logger
    session_log = logging.getLogger(f"{APP_NAME}.wss:" + session["id"])
    session_log.setLevel(INFO)
    handler = logging.FileHandler(f"logs/{session['id']}.log")
    formatter = logging.Formatter(f"{session_id} %(levelname)s %(message)s")
    handler.setFormatter(formatter)
    session_log.addHandler(handler)

    session_log.info(f"New WS connection from {addr}, assigned session id: {session['id']}")

    while True:
        try:
            body = ws.receive(timeout=WS_TIMEOUT)
            if body is None:
                session_log.info(f"Session timed out after {WS_TIMEOUT}s")
                break

            if body == "":
                continue
            msg = flask.json.loads(body)
            method = msg["type"]
            session_log.debug(f"request: {msg}")

            if method == "info":
                ws.send(
                    flask.json.dumps(
                        {
                            "type": "info",
                            "session_id": session["id"],
                            "coins": session["coins"],
                            "spin_cost": SPIN_COST,
                            "flag_price": FLAG_PRICE,
                            "win_payout": SPIN_COST * PAYOUT_MULTIPLIER,
                        }
                    )
                )
            elif method == "spin":
                if session["coins"] >= SPIN_COST:
                    session["coins"] -= SPIN_COST
                    roll = [random.randint(0, 9) for i in range(3)]
                    if roll[0] == roll[1] == roll[2]:
                        session["coins"] += SPIN_COST * PAYOUT_MULTIPLIER
                        info = flask.json.dumps(
                            {
                                "type": "spin",
                                "coins": session["coins"],
                                "roll": roll,
                                "prize": SPIN_COST * 5,
                                "win": True,
                            }
                        )
                        session_log.info(
                            f"Player won! What an incredible achievement. {addr=}, {msg=}, {info=}"
                        )
                        ws.send(info)
                    else:
                        ws.send(
                            flask.json.dumps(
                                {
                                    "type": "spin",
                                    "coins": session["coins"],
                                    "roll": roll,
                                    "win": False,
                                }
                            )
                        )
                else:
                    session_log.info(
                        f"Player is broke, you should probably pull yourself up by the bootstraps {addr=}, {msg=}"
                    )
                    ws.send(
                        flask.json.dumps(
                            {
                                "type": "error",
                                "message": "You are broke, come back when you got some more money.\nYou need more than 20 coins to spin!",
                            }
                        )
                    )

            elif method == "flag":
                if session["coins"] >= FLAG_PRICE:
                    session["coins"] -= FLAG_PRICE
                    ws.send(flask.json.dumps({"type": "flag", "flag": open("flag.txt").read()}))
                    app.logger.warning(f"Someone got the flag! {addr=}, {msg=}")
                elif session["admin"] == True:
                    session["flag"] = open("flag.txt").read()
                    app.logger.warning(f"Admin got the flag! {addr=}, {msg=}")
                else:
                    session_log.info(
                        f"An uncualified player tried to get the flag, you should probably just give up. {addr=}, {msg=}"
                    )
                    ws.send(
                        flask.json.dumps(
                            {
                                "type": "error",
                                "message": "You need more than 1 million coins to get the flag!",
                            }
                        )
                    )

            # admin api
            elif method == "login":
                if verify_admin(msg.get("password", "")):
                    session_log.info(f"Admin logged in, welcome back me! {addr=}")
                    session["admin"] = True
                    ws.send(flask.json.dumps({"type": "admin", "message": "Logged in"}))
                else:
                    session_log.info(f"Admin login failed, you are not me! {addr=}, {msg=}")
                    ws.send(
                        flask.json.dumps({"type": "error", "message": "Invalid authentification"})
                    )
            elif method == "logout":
                session.pop("admin")
                ws.send(flask.json.dumps({"type": "admin", "message": "Logged out"}))
            elif method == "debug":
                if session.get("admin", False):
                    session_log.setLevel(DEBUG)
                    ws.send(flask.json.dumps({"type": "admin", "message": "Debug mode enabled"}))
            elif method == "motherload":
                if session.get("admin", False) and verify_knowledge(msg["password"]):
                    session["coins"] += FLAG_PRICE * 100
                    app.logger.warning(
                        f"Motherload activated by {addr=} look at this guy, money is literally falling out of his pockets. msg: {msg}, session: {session['id']}, session: {session}"
                    )
                    ws.send(
                        flask.json.dumps(
                            {
                                "type": "admin",
                                "message": "Motherload activated!",
                                "coins": session["coins"],
                            }
                        )
                    )
                else:
                    ws.send(
                        flask.json.dumps({"type": "admin", "message": "Invalid authentification"})
                    )
            else:
                ws.send(flask.json.dumps({"type": "error", "message": "Unknown method"}))

        except ConnectionClosed:
            break
        except JSONDecodeError or TypeError:
            session_log.warning(f"Invalid JSON from {addr=}")
            ws.send(flask.json.dumps({"type": "error", "message": "Invalid JSON"}))
        except Exception:
            session_log.debug(f"User state: {session=}")
            session_log.exception(f"Error from {addr=}:")
            ws.send(
                flask.json.dumps(
                    {
                        "type": "error",
                        "message": "Don't be mean to the server, it got feelings 2 :(",
                    }
                )
            )

    del session_log
    # clean up old session logs
    # remove all logs older than LOG_KEEP_TIME seconds
    for f in os.listdir("logs"):
        if time.time() - os.path.getmtime(f"logs/{f}") > LOG_KEEP_TIME:
            os.remove(f"logs/{f}")

    ws.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, threaded=True, ssl_context='adhoc')

import os
from flask import Flask, request

app = Flask(__name__)
FLAG = os.getenv('FLAG')


@app.route('/flag')
def flag():
    secret = request.headers.get('secret')
    if secret == "SuPerSecRetPasSwOrd":
        return FLAG, 200

    return "Access denied", 403


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=8090)

import os
import random
from flask import Flask, session, render_template

flag = os.environ.get('FLAG', 'FLAG{NOT_SET}')

app = Flask(__name__, instance_relative_config=True, template_folder="./")
app.secret_key = str(random.randint(10000, 99999))

@app.route('/', methods=['GET'])
def hello():
    if 'clicks' not in session:
        session['clicks'] = 0
        session['isAdmin'] = False

    return render_template('index.html', clicks=session.get('clicks', 0))

@app.route('/click', methods=['GET'])
def click():
    session['clicks'] = session.get('clicks', 0) + 1
    return 'OK'

@app.route('/flag', methods=['GET'])
def get_flag():
    if "isAdmin" not in session or session["isAdmin"] != True:
        return "You are not an admin!"

    return flag


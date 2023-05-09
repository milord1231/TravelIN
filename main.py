from flask import *

from datetime import datetime

import os

from flask_sqlalchemy import SQLAlchemy

import requests

from datetime import date

import random

from flask import Flask, request


application = Flask(__name__)

app = application

app.config['SECRET_KEY'] = 'rapideboost'

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4'}

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///base.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



@app.before_first_request
def before_first_request():
    print(session)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')




if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    application.run(host='0.0.0.0')



# 0 - BOOST 5x5 (BOTS)

# 1 - BOOST 5x5 (LOBBY)

# 2 - BOOST 2x2 (BOTS)

# 3 - BOOST 2z2 (LOBBY)

# 4 - BOOST KD  (BOTS)

# 5 - BOOST KD  (CHEAT)

# 6 - FOR ALL BOOST
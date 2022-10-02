import email
from urllib import request
from xml.dom.minidom import Document
from flask import render_template, Blueprint, Flask
import dataCapture as dc
import pandas as pd
bp = Blueprint('main', __name__)

@bp.route('/')
def base():

    return render_template("home.hl")

@bp.route('/home')
def home():

    return render_template("home.hl")

@bp.route('/loggedIn')
def LoggedIn():

    return render_template("loggedIn.hl")

@bp.route('/signUp')
def SignUp():
    if request.method == "POST":
        df = dc.readUserData("userData.pkl")
        request.form.get(email)


    return render_template("signUp.hl")

@bp.route('/about')
def about():

    return render_template("about.hl")

app = Flask(__name__)
app.register_blueprint(bp)
app.add_url_rule('/', endpoint='base')
app.add_url_rule('/home', endpoint='home')
app.add_url_rule('/about', endpoint = 'about')
app.add_url_rule('/loggedIn', endpoint='loggedIn')
app.add_url_rule('/signUp', endpoint='signUp')
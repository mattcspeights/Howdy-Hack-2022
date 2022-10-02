from crypt import methods
import email
from xml.dom.minidom import Document
from flask import render_template, Blueprint, Flask, request
import dataCapture as dc
import pandas as pd
bp = Blueprint('main', __name__)

@bp.route('/', methods=['POST', 'GET'])
def base():
    if request.method == "POST":
        email = request.form.get("email")
        print(email)
    return render_template("home.hl")

@bp.route('/home', methods=['POST', 'GET'])
def home():

    return render_template("home.hl")

@bp.route('/loggedIn', methods=['POST'])
def LoggedIn():

    return render_template("loggedIn.hl")

@bp.route('/signUp', methods=['POST'])
def SignUp():

    return render_template("home.hl")

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
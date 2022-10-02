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
    if request.method == "POST":
        df = dc.readUserData("userData.pkl")
        #get data from webpage
        Username = request.form.get("uname")
        UserPass = request.form.get("pword")
        #check if the password matches
        if dc.checkPass(df, Username, UserPass) == -1:
            pass
        else:
            return render_template("loggedIn.hl")
    #update with where the user gets redirected if pass or uname is wrong
    return render_template("loggedIn.hl")

@bp.route('/signUp')
def SignUp():
    if request.method == "POST":
        df = dc.readUserData("userData.pkl")
        #request the elements from the webpage
        UserEmail = request.form.get("email")
        UserAddress = request.form.get("address")
        Username = request.form.get("uname")
        UserPass = request.form.get("pword")
        #validate username
        if dc.inDf(df, Username):
            pass
        else:
            #take collected info and add a new user
            dc.addUserInfo(df, Username, UserEmail, UserPass, UserAddress)
        #write new data into file
        dc.writeUserData(df, "userData.pkl")
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
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

@bp.route('/signUp', methods=['POST'])
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
from crypt import methods
import email
from xml.dom.minidom import Document
from flask import render_template, Blueprint, Flask, request, url_for, redirect
import dataCapture as dc
import pandas as pd
import requests as http

bp = Blueprint('main', __name__)

@bp.route('/', methods=['POST', 'GET'])
def base():
    if request.method == "POST":
        df = dc.readUserData("userData.pkl")
        #request the elements from the webpage
        Username = request.form.get("uname")
        UserPass = request.form.get("pword")
        
        #validate username
        if dc.checkPass(df, Username, UserPass):
            print("valid")
            return redirect(url_for('loggedIn'))
        else:
            print("not valid")
            return redirect(url_for('base'))

    return render_template("home.hl")

@bp.route('/loggedIn', methods=['POST', 'GET'])
def LoggedIn():
    return render_template("loggedIn.hl")

@bp.route('/signUp', methods=['POST', 'GET'])
def SignUp():
    if request.method == "POST":
        print("signup")
        df = dc.readUserData("userData.pkl")
        #request the elements from the webpage
        UserEmail = request.form.get("email")
        UserAddress = request.form.get("address")
        Username = request.form.get("fname")
        UserPass = request.form.get("pword")
        #validate username
        if dc.inDf(df, Username):
            print("invalid username")
            userExists = True
            return render_template("signUp.hl", userExists=userExists)
        else:
            #take collected info and add a new user
            dc.addUserInfo(df, Username, UserEmail, UserPass, UserAddress)
            #write new data into file
            dc.writeUserData(df, "userData.pkl")
            return redirect(url_for('base'))
            # return render_template("home.hl")
    else:
        return render_template("signUp.hl")

@bp.route('/about')
def about():

    return render_template("about.hl")

app = Flask(__name__)
app.register_blueprint(bp)
app.add_url_rule('/', endpoint='base')
app.add_url_rule('/about', endpoint = 'about')
app.add_url_rule('/loggedIn', endpoint='loggedIn')
app.add_url_rule('/signUp', endpoint='signUp')
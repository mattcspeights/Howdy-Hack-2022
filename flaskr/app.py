from crypt import methods
import email
from xml.dom.minidom import Document
from flask import render_template, Blueprint, Flask, request, url_for, redirect
import dataCapture as dc
import matchUsers as match
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
        if dc.checkPass(df, Username, UserPass) == 1:
            print("valid")
            return redirect(url_for('loggedIn') + f'?username={Username}')
        else:
            print("not valid")
            return redirect(url_for('base'))

    return render_template("home.hl")

@bp.route('/loggedIn', methods=['POST', 'GET'])
def LoggedIn():
    UserName = ""
    if request.method == "POST":
        df = dc.readUserData('userData.pkl')
        #get data from drop down menues
        UserName = request.args.get("username")
        destination = request.args.get("destination")
        hours = request.form.get("hours")
        print(hours)
        mins = request.form.get("mins")
        print(mins)
        ampm = request.form.get("time")
        print(ampm)
        dc.modifyDestination(df, UserName, destination, hours, mins, ampm)
        print(df)
        #print(match.matchUsers(df, UserName))

        return redirect(url_for('matches') + f"?username={UserName}")

    

    return render_template("loggedIn.hl", UserName=request.args.get("username"))

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
    else:
        return render_template("signUp.hl")

@bp.route('/matches', methods=['POST', 'GET'])
def matches():
    if request.method == 'POST':
        df = dc.readUserData('userData.pkl')
        UserName = request.args.get('username')
        userList = match.matchUsers(df, UserName)

        return render_template('matches.hl', riderList=userList)

    return render_template('matches.hl')

@bp.route('/about')
def about():

    return render_template("about.hl")

app = Flask(__name__)
app.register_blueprint(bp)
app.add_url_rule('/', endpoint='base')
app.add_url_rule('/about', endpoint = 'about')
app.add_url_rule('/loggedIn', endpoint='loggedIn')
app.add_url_rule('/signUp', endpoint='signUp')
app.add_url_rule('/matches', endpoint='matches')
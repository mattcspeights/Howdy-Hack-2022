import pandas as pd
import hashlib
import pickle

'''
Frame Data:

username: must be unique
email
password: encrypt
seats: int fo seats available
origin:string
destination:string
passengers: other users that are riding with 
'''

def hashPass(password):
    hashedPass = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashedPass

df = pd.read_pickle("userData.pkl")

def findUserIndex(username):
    return df[df["User Name"] == username].index.values[0]

def inDf(username):
    if username in df["User Name"].unique():
        return True

def storePassword(username, password, df):
    # hash password

    df.loc[findUserIndex(username), "Password"] = hashPass(password)

def getPassword(index):
    return df.iloc[index]["Password"]

"""
return codes:
-1: Login information invalid
1: Successful login
"""
def checkPass(username, password):
    if not inDf(username):
        return -1
    if getPassword(findUserIndex(username)) == hashPass(password):
        return 1
    
def addUserInfo(userData, username, email, password, seats, origin, destination, passengers):
    userData.loc[len(userData.index)] = [username, email, hashPass(password), seats, origin, destination, passengers]

addUserInfo(df, "matthew", "mattcspeights@gmail.com", "123", "4", "", "test", "test")


import pandas as pd
import hashlib
import pickle
import numpy as np

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

def HashPass(password):
    hashedPass = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashedPass

df = pd.read_pickle("userData.pkl")

def storePassowrd(username, password, df):
    # hash password

    df.loc[np.where(df["User Name"] == username)][password] = password

def findUser(username):
    print(df[df["User Name"] == username]["Password"][0])

df.loc[len(df.index)] = ['matthew', 'test', '12345', 'test', 'test', 'test', 'test']

findUser("matthew")

storePassowrd("matthew", "cheeseBawls", df)

findUser("matthew")
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

def HashPass(password):
    hashedPass = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashedPass

df = pd.read_pickle("userData.pkl")


print(df)

def findUser(username):
    print(df[df["User Name"] == username])

df.loc[len(df.index)] = ['matthew', 'test', '12345', 'test', 'test', 'test', 'test']

findUser("matthew")
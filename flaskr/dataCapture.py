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

def findUserIndex(df, username):
    if len(df[df["User Name"] == username].index.values) == 0:
        return 0
    return df[df["User Name"] == username].index.values[0]

def inDf(df, username):
    if username in df["User Name"].unique():
        return True

def storePassword(username, password, df):
    df.loc[findUserIndex(df,username), "Password"] = hashPass(password)

def getPassword(df, index):
    return df.iloc[index]["Password"]

"""
return codes:
-1: Login information invalid
1: Successful login
"""
def checkPass(df, username, password):
    if not inDf(df, username):
        return -1
    if getPassword(df, findUserIndex(df, username)) == hashPass(password):
        return 1
    else:
        return -1
    
def addUserInfo(userData, username, email, password, origin):
    userData.loc[len(userData.index)] = [username, email, hashPass(password), 0, origin, ["","","",""], []]

def modifySeats(df, username, seats):
    df.loc[findUserIndex(df,username), "Seats"] = seats

def modifyDestination(df, username, destination, hour, mins, ampm):
    df.loc[findUserIndex(df,username), "Destination"][0] = destination
    df.loc[findUserIndex(df,username), "Destination"][1] = hour
    df.loc[findUserIndex(df,username), "Destination"][2] = mins
    df.loc[findUserIndex(df,username), "Destination"][3] = ampm
    writeUserData(df, 'userData.pkl')

def modifyPassengers(df, username, passengers):
    df.loc[findUserIndex(df,username), "Passengers"].append(passengers)

def readUserData(filename):
    df = pd.read_pickle(filename)
    return df

def writeUserData(df, filename):
    df.to_pickle(filename)

# df = readUserData("userData.pkl")

#addUserInfo(df, "killian", "killian@gmail.com", "Password", "Your moms house")

#modifySeats(df, "killian", 3)
#modifyDestination(df, "killian", "Your dads house")
#modifyPassengers(df, "killian", ["evan", "tyler"])

# print(df)

# df = pd.DataFrame(columns=['User Name', 'Email', 'Password', 'Seats', 'Origin', 'Destination', 'Passengers'])

# writeUserData(df, "userData.pkl")

# print(df)
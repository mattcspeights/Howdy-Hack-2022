import pandas as pd
from dataCapture import findUserIndex

def matchUsers(df, username):
    destination = df.iloc[findUserIndex(username)]["Destination"]
    matchedUsers = []

    matchFrame = df[df["Destination"] == destination]

testFrame = {}
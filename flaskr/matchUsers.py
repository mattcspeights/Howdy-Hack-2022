import pandas as pd
from dataCapture import findUserIndex

def matchUsers(df, username):
    destination = df.iloc[findUserIndex(username)]["Destination"]
    matchedUsers = []

    for i in range(len(df.index)):
        pass
import pandas as pd
#from dataCapture import findUserIndex
import dataCapture as dc

def matchUsers(df, username):
    destination = df.iloc[dc.findUserIndex(df, username)]["Destination"][0]
    matchedUsers = []

    for i in range(len(df.index)):
        if df.iloc[i]["User Name"] != username and df.iloc[i]["Destination"][0] == destination:
            tempdf = df.iloc[i]
            matchedUsers.append({'Username' : tempdf["User Name"],
            'Email' : tempdf["Email"], 
            'Origin' : tempdf["Origin"],
            'Destination' : tempdf["Destination"]})

#email, destination, origin, username
    return matchedUsers

#testFrame = dc.readUserData("userData.pkl")

#dc.addUserInfo(testFrame, "killian", "killian@gmail.com", "Password", "Your moms house")

#dc.modifySeats(testFrame, "killian", 3)
#dc.modifyDestination(testFrame, "killian", "Your dads house")
#dc.modifyPassengers(testFrame, "killian", ["evan", "tyler"])
#dc.modifyDestination(testFrame, "admin", "Your dads house")

#users = matchUsers(testFrame, "admin")

#print(users)
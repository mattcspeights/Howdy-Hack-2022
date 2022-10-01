import pandas as pd
from hashlib import sha256
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

df = pd.read_pickle("userData.pkl")


print(df)

df.to_pickle('userData.pkl')

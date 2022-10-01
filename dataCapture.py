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

df = pd.read_
#pd.DataFrame(columns=['User Name', 'Email', 'Password', 'Seats', 'Origin', 'Destination', 'Passengers'])

print(df)

df.to_csv('user_data.csv', index=False)

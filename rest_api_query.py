import requests
import json
import os

login = json.load(open("login_info.json"))          # These 2 json files are not included 
database = json.load(open("heart_rate_info.json"))  # in the repo for privacy reasons

login_url = database['login']
heartrate_data_url = database['heart_rate_all']

user = login['email'].split('@')[0] #Get the user for folder creation
response = requests.post(login_url, data=login)
access_token = response.json()['data']['access_token']

headers = {"Authorization": "Bearer " + access_token}
response = requests.get(heartrate_data_url, headers=headers)

try:
    os.mkdir(user)
except:
    print("Could not create directory")

with open(user + '/data.json', 'w') as outfile:
    json.dump(response.json(), outfile)
import requests
import json
import os
import time

login_info = json.load(open("login_info.json"))
api_info = json.load(open("api_urls.json"))


def user_login(email, password):
    login_url = login_info["api"] + "/login"
    response = requests.post(login_url, data={"email": email, "password": password})
    access_token = response.json()['data']['access_token']
    return access_token

def get_activity(token, activity_type, from_to_tuple=None):
    if from_to_tuple is None:  # Get all activity data
        activity_data_url = api_info["heart_rate_all"].replace("{api}", login_info["api"])
        response = requests.get(activity_data_url, headers={"Authorization": "Bearer " + token})
        return response
    else:
        pass

def get_heartrate(token, from_to_tuple=None):
    if from_to_tuple is None:  # Get all heartrate data
        heartrate_data_url = api_info["heart_rate_all"].replace("{api}", login_info["api"])
        response = requests.get(heartrate_data_url, headers={"Authorization": "Bearer " + token})

    else:
        start, end = from_to_tuple
        pass

def get_questionaire(token, from_to_tuple=None):
    if from_to_tuple is None: # Get latest
        questionaire_data_url = api_info["questionanaires"].replace("{api}", login_info["api"]).replace("{questionnaire}", "big_five")
        response = requests.get(questionaire_data_url, headers={"Authorization": "Bearer " + token})
        return response
    else:
        start, end = from_to_tuple
        pass
if __name__ == "__main__":
    token = user_login(login_info["email"], login_info["password"])

    get_heartrate(token)
    activity = get_activity(token, "walking", (0, 1623929554791))
    quest = get_questionaire(token)
    pass

import requests
import json
import os
import time
import sys

login_info = json.load(open("login_info.json"))
api_info = json.load(open("api_urls.json"))


def calculate_pts_score(conscientiousness, neuroticism):
    if conscientiousness >= 4.5:
        if neuroticism >= 4.5:
            return 3
        else:
            return 1
    elif conscientiousness >= 3.1:
        if neuroticism >= 4.5:
            return 3
        elif neuroticism > 3.95:
            return 2
        else:
            return 1
    else:
        if neuroticism > 3.95:
            return 3
        elif neuroticism >= 2.2:
            return 2
        else:
            return 1


def user_login(email, password):
    login_url = login_info["api"] + "/login"
    response = requests.post(login_url, data={"email": email, "password": password})
    access_token = response.json()['data']['access_token']
    return access_token


def get_activity(token, activity_type, from_to_tuple=None):
    if from_to_tuple is None:  # Get all activity data
        return None
    else:
        start, end = from_to_tuple
        activity_data_url = api_info["activity"].replace("{api}", login_info["api"]).replace("{activity}",
                                                                                             activity_type).replace(
            "{from}", str(start)).replace("{to}", str(end))
        response = requests.get(activity_data_url, headers={"Authorization": "Bearer " + token})
        return response.json()


def get_current_activity(token):
    # duration = (int(time.time())-3600, int(time.time())) # Get all activities in the latest hour
    duration = (0, int(time.time()))

    possible_actions = ["walking", "running", "still"]
    recent_activities = []

    for act in possible_actions:
        temp_act = get_activity(token, act, duration)["data"]
        if len(temp_act) > 0:
            recent_activities.append(temp_act[-1])

    current_activity = max(recent_activities, key=lambda k: k["end_time"])
    return current_activity["activity"]

def get_heartrate(token, from_to_tuple=None):
    if from_to_tuple is None:  # Get all heartrate data
        heartrate_data_url = api_info["heart_rate_all"].replace("{api}", login_info["api"])
        response = requests.get(heartrate_data_url, headers={"Authorization": "Bearer " + token})

    else:
        start, end = from_to_tuple
        heartrate_data_url = api_info["heart_rate_from_to"].replace("{api}", login_info["api"]).replace(
            "{from}", str(start)).replace("{to}", str(end))
        response = requests.get(heartrate_data_url, headers={"Authorization": "Bearer " + token})
        pass
    return response.json()


def get_current_heartrate(token):
    duration = (0, int(time.time()))

    data = get_heartrate(token, duration)["data"]
    return data[-1]["heart_rate"]


def get_questionnaire(token, from_to_tuple=None):
    if from_to_tuple is None:  # Get latest
        questionaire_data_url = api_info["questionanaires"].replace("{api}", login_info["api"]).replace(
            "{questionnaire}", "big_five")
        response = requests.get(questionaire_data_url, headers={"Authorization": "Bearer " + token})
        return response.json()
    else:
        start, end = from_to_tuple
        pass


if __name__ == "__main__":
    token = user_login(login_info["email"], login_info["password"])

    bpm = get_current_heartrate(token)
    activity = get_current_activity(token)

    quest = get_questionnaire(token)
    conscientiousness, neuroticism = quest["data"]["conscientiousness"], quest["data"]["negative_emotionality"]
    pts = calculate_pts_score(conscientiousness, neuroticism)

    threshold = 80
    if bpm > 80:
        if activity is "running" or activity is "walking":
            pass
    else:
        pts = pts+1

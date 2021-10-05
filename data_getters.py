import requests
import json
import os

login_info = json.load(open("login_info.json"))


def user_login(email, password):
    login_url = login_info["api"] + "/login"
    response = requests.post(login_url, data={"email": email, "password": password})
    access_token = response.json()['data']['access_token']
    return access_token


def get_heartrate(token, from_to_tuple=None):
    if from_to_tuple is None:  # Get all heartrate data
        headers = {"Authorization": "Bearer " + token}
        heartrate_data_url = login_info["api"] + "/login"
        response = requests.get(heartrate_data_url, headers=headers)
        pass
    else:
        start, end = from_to_tuple

        pass


if __name__ == "__main__":
    token = user_login(login_info["email"], login_info["password"])

    get_heartrate(token, (0, 1000))

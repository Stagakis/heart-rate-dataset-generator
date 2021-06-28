import json
import glob

folders = glob.glob("worker*")

for folder in folders:
    database = json.load(open(folder + "/data.json"))  # in the repo for privacy reasons
    heart_rate_data = []
    timestamp_data = []
    for data in database['data']:
        heart_rate_data.append(data['heart_rate'])
        timestamp_data.append(data['start_time'])
    print(heart_rate_data)
    with open(folder + '/heart.txt', 'w') as outfile:
        for measurement in heart_rate_data:
            outfile.write("%s\n" % measurement)
    with open(folder + '/timestamps.txt', 'w') as outfile:
        for measurement in timestamp_data:
            outfile.write("%s\n" % measurement)
import json
import csv
import requests

url = "https://api-url.cyren.com/api/v1/free/urls-list"

# Payload Format...
# payload = json.dumps({
# "urls": [
# "google.com",
# "youtube.com"
# ]
# })

payload = open('./urls.txt', 'r')
payload = payload.read()
payload = payload.splitlines()

payloadInfo = {
    "urls": payload
}

payloadInfo = json.dumps(payloadInfo)

# Header File Consisting of API Token [Bearer <api Token>]

headers = {
    'Authorization': 'Bearer <Your Cyren JSON Web Token>',
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payloadInfo)
# print(response.text)

jsonData = json.loads(response.text)
info = jsonData["urls"]

data_file = open("result.csv", 'w')

csv_writer = csv.writer(data_file)
count = 0

for data in info:
    if count == 0:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1
    data["categoryNames"] = data["categoryNames"][0]
    csv_writer.writerow(data.values())

data_file.close()
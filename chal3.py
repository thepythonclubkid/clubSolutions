# Sean
# July 2013

import requests
import json
import base64

url = "http://thepythonclub.org:8083/challenge3"
responce = requests.get(url)
words = responce.content.rsplit('"')

# Get user name
user = words[1]

# Get users
usersURL = words[3]
usersPage = requests.get(usersURL).content
users = json.loads(usersPage)

# Find userID from userName
userID = 0
for key in users:
    if users[key]['Name'] == user:
        userID = key
        break

# Get passwords
passwordURL = words[5]
passwordsPage = requests.get(passwordURL).content
passwords = json.loads( passwordsPage)

# Find password for userID
password = ''
for key in passwords:
    if key == userID:
        password = base64.b64decode(passwords[key])
        break

url_answer = "http://thepythonclub.org:8083/challenge3"
payload = {'answer':password}
responce = requests.post(url, data = json.dumps(payload))
print("Responce: " + responce.content)

# Sean
# July 2013

import base64
import requests
import json

url = "http://melodicbios.com:8081/challenge1"
responce = requests.get(url)

encodedString = responce.content.rsplit('"')[1]
answer = base64.b64decode(encodedString)

payload = {'answer':answer}
responce = requests.post(url, data = json.dumps(payload))

print("Answer: " + responce.content)

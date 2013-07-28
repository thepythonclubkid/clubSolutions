# Sean
# July 2013

import requests
import json

numbers = { 
    'one':   1, 'eleven':     11, 'ten': 10,
    'two':   2, 'twelve':     12,
    'three': 3, 'thirteen':   13,
    'four':  4, 'fourteen':   14,
    'five':  5, 'fifteen':    15,
    'six':   6, 'sixteen':    16,
    'seven': 7, 'seventeen':  17,
    'eight': 8, 'eighteen':   18,
    'nine':  9, 'nineteen':   19 
}

rev_numbers = {
    1:'one',    6:'six',    11:'eleven',
    2:'two',    7:'seven',  12:'twelve',
    3:'three',  8:'eight',  13:'thirteen',
    4:'four',   9:'nine',   14:'fourteen',
    5:'five',   10:'ten',   15:'fifteen'
}

url = "http://thepythonclub.org:8082/challenge2"
responce = requests.get(url)
questionString = responce.content.rsplit('"')[1]

words = questionString.rsplit()
firstNumber = words[0]
secondNumber = words[2]
thirdNumber = words[4]

first = numbers[firstNumber]
second = numbers[secondNumber]
third = numbers[thirdNumber]

firstOperator = words[1]
secondOperator = words[3]

# First operation
if firstOperator == "minus":
    intero = first - second
else:
    intero = first + second

# Second operation
if secondOperator == "minus":
    final = intero - third
else:
    final = intero + third

url_answer = "http://thepythonclub.org:8082/challenge2"
payload = {'answer':rev_numbers[final]}
responce = requests.post(url, data = json.dumps(payload))
print("Answer: " + responce.content)

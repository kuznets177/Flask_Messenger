import dataclasses
import requests
from flask import request

response = requests.get('http://127.0.0.1:5000/status')

if response.json():
    username = input('Enter your name: ')
    password = input('Enter your password: ')

    login_data = {
    'username': username,
    'password': password
    }

response = requests.post('http://127.0.0.1:5000/login', json=login_data)

# check if user isn't registered
response_login_data = str(response.json())
if response_login_data[-6:-1] == 'False':
    requests.post('http://127.0.0.1:5000/register', json=login_data)
    print(response.json())

while True:
    text = input()
    data = {
        'username': username,
        'password': password,
        'text': text
    }

    requests.post('http://127.0.0.1:5000/login', json=login_data)
    response = requests.post('http://127.0.0.1:5000/send', json=data)
    print(response.json())


import hashlib
import time
from datetime import datetime
from flask import Flask, request


app = Flask(__name__)
# добавляем hash, чтобы пароли не хранились в открытом виде
def make_password_hash(password):
    m = hashlib.md5()
    m.update(password.encode('utf-8'))
    return m.hexdigest()


messages = [
    {'username': 'Jonh', 'time': time.time(), 'text': 'Hello!', 'receiver': 'All'},
    {'username': 'Mary', 'time': time.time(), 'text': 'Oh, hi John', 'receiver': 'Danil'},
]
users = {
    # username: password hash
    "John": make_password_hash("Wick"), "Mary": make_password_hash("Mary")
}


@app.route("/")
def hello_kl():
    return "Добро пожаловать!"


@app.route("/status")
def status_kl():
    return {'status': True, 'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'messages_count': len(messages),
            'users_count': len(users)
            }


@app.route("/messages")
def messages_kl():
    """
    :input: ?after = float
    :return: [{'username': str, 'time': float, 'text': str}, ...]
    """
    print(request.args)
    after = float(request.args['after'])

    filtered_messages = []
    for message in messages:
        if message['time'] > after:
            filtered_messages.append(message)

    return {'messages': filtered_messages}


@app.route("/send", methods=['POST'])
def send_kl():
    """
    отправить сообщение всем.
    :input: {"username": str, "password": str, "text": str"}
    :return:{"ok": bool}
    """
    print(request.json)
    username = request.json["username"]
    password = request.json["password"]
    text = request.json["text"]

    if username not in users or users[username] != password:
        return{'ok': False}

    messages.append({'username': username, 'time': time.time(), 'text': text}),
    return{'ok': True}


@app.route("/login", methods=['POST'])
def login_kl():
    """
    отправить сообщение всем.
    :input: {"username": str, "password": str}
    :return:{"ok": bool}
    """
    print(request.json)
    username = request.json["username"]
    password = request.json["password"]

    if username not in users:
        users[username] = password
        return {'ok': True}
    elif users[username] == password:
        return {'ok': True}
    else:
        return{'ok': False}

app.run()
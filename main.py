from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to my system, Please login'

@app.route('/login/<username>')
def login(username):
    try:
        with open('config.json') as users:
            user_list = json.load(users)
    except:
        return 'Error: Config file missing'
    if username in user_list:
        return 'Access granted'
    else:
        return 'Access denied'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80)

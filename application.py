from flask import Flask

application = Flask(__name__)

@application.route('/')
def hello_world():
    return "HELLO WORLD"

@application.route('/hello')
def hello_world():
    return "HELLO WORLD"

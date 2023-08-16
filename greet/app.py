from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def rootPage():
    return f"<h1>Welcome To root</h1>"

@app.route('/welcome')
def welcome():
    return f"<h1>Welcome</h1>"

@app.route('/welcome/home')
def welcomeHome():
    return f"<h1>Welcome Home</h1>"

@app.route('/welcome/back')
def welcomeBack():
    return f"<h1>Welcome Back</h1>"





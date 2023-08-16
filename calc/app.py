from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def rootPage():
    return f"<h1>Welcome To root</h1>"

@app.route('/add')
def add():
    a = int(request.args['a'])
    
    b = int(request.args['b'])
    c = a + b
    
    return f"{c}"

@app.route('/sub')
def sub():
    a = int(request.args['a'])
    
    b = int(request.args['b'])
    c = a - b
    
    return f"{c}"

@app.route('/mult')
def mult():
    a = int(request.args['a'])
    
    b = int(request.args['b'])
    c = a * b
    
    return f"{c}"

@app.route('/div')
def div():
    a = int(request.args['a'])
    
    b = int(request.args['b'])
    c = a / b
    
    return f"{c}"
# Put your app in here.

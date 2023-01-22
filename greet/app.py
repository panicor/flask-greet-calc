from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    return "Welcome"

@app.route("/welcome/home")
def home():
    return "Welcome home"

@app.route("/welcome/back")
def returning():
    return "Welcome back"

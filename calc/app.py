# Put your app in here.
from flask import Flask,request
from operations import add,sub,mult,div

app = Flask(__name__)


operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route("/math/<operation>")
def math(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[operation](a, b)
    return str(result)


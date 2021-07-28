from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/hello/")

@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/index/")
def index(name = None):
    return render_template(
        "index.html",
        name=name,
        date=datetime.now()
    )

if __name__ == '__main__':
    app.run(debug = True) 

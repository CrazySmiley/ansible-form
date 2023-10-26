from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>New, version 2.0!</p>"


#!/usr/bin/python3
"""
A script that starts a Flask web application
The web application listens on 0.0.0.0 and port 5000
"""

from flask import Flask

app = Flask(__name__)
IP = "0.0.0.0"
Port = 5000

@app.route("/", strict_slashes = False)
def hello_hbnb():
    return "<h1>Hello HBNB</h1>"

@app.route("/hbnb", strict_slashes = False)
def hbnb():
    return "<h1>HBNB</h1>"
if __name__ == "__main__":
    app.run()

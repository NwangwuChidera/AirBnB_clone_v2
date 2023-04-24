#!/usr/bin/python3
"""
A script that starts a Flask web application
The web application listens on 0.0.0.0 and port 5000
"""
from flask import Flask

app = Flask("__name__")


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return ("hello HBNB!")

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return ("HBNB")

@app.route("/c/<text>", strict_slashes=False)
def c_content(text ="is_cool"):
    """replace _ with an empty space"""
    return "C {}".format(text.replace("_", " "))

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonText(text="is cool"):
    """display Python followed by the value of the text variable"""
    return "Python {}".format(text.replace("_", " "))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)

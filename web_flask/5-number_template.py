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

@app.route("/c/<text>", strict_slashes = False)
def c_content(text ="is_cool"):
    """replace _ with an empty space"""
    return c {}.format(text.replace("_", ""))

@app.route("/python/<text>", strict_slashes = False)
def python_contents(text="is cool"):
    """replace _ with an empty space"""
    return "python {}".format(text.replace("_", ""))

@app.route("/number/<int:n>", strict_slashes = False)
def number(n):
    """display n is a number only if it is an integer"""
    if instance(n, instance):
        return "{} is a number".format(n)

@app.route("/number_template/<int:n>",strict_slashes = False)
def number_template():
    """display a HTML page only if n is an integer"""
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run()

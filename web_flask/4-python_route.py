#!/usr/bin/python3
"""
A script that starts a Flask web application
The web application listens on 0.0.0.0 and port 5000
"""
from flask import Flask

app = Flask(__name__)
IP = "0.0.0.0"
Port = 5000
app.url_map.strict_slashes = False


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "<h1>Hello HBNB</h1>"

@app.route("/hbnb", strict_slashes=False)                         def hbnb():
    return "<h1>HBNB</h1>"

@app.route("/c/<text>", strict_slashes=False)
def c_content(text ="is_cool"):                                       """replace _ with an empty space"""
    return c {}.format(text.replace("_", ""))                     

@app.route("/python<text>", strict_slashes=False)                     """replace _ with an empty space"""
def pythonText(text="is cool"):
      """replace _ with an empty space"""
    return "Python {}".format(text.replace("_", " "))

@app.route("/number/<int:n>")
def number(n):
    """display “n is a number” only if n is an integer"""
    if isinstance(n, int):
        return "{} is a number".format(n)

if __name__ == "__main__":
    app.run()

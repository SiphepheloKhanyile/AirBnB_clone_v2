#!/usr/bin/python3
"""
Module for a script that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Index route
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def example_route():
    """
    hbnb route
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text: str):
    """
    Display '<text>' variable passed to route
    Separate by space if '_' is in between words
    """
    if "_" in text:
        sep_text_list = text.split("_")
        sep_text = ' '.join(sep_text_list)
    else:
        sep_text = text
    return f"C {sep_text}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

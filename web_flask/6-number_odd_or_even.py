#!/usr/bin/python3
"""
Module for a script that starts a Flask web application
"""
from flask import Flask, render_template

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


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_route(text: str = 'is cool'):
    """
    Display “Python ”, followed by the value of the text variable
    (replace underscore _ symbols with a space )
    default value of `text` is 'is cool'
    """
    if "_" in text:
        sep_text_list = text.split("_")
        sep_text = ' '.join(sep_text_list)
        return f"Python {sep_text}"

    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n: int):
    """
    Display “n is a number” only if n is an integer
    """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n: int):
    """
    Display a HTML page only if n is an integer:
        H1 tag: “Number: n” inside the tag BODY
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n: int):
    """
    Display a HTML page only if n is an integer:
        H1 tag: `“Number: n is even|odd”` inside the tag `BODY`
    """
    if (n % 2) == 0:
        return render_template('6-number_odd_or_even.html',
                               number=n, answer='even')

    return render_template('6-number_odd_or_even.html',
                           number=n, answer='odd')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

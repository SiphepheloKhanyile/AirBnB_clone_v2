#!/usr/bin/python3
"""
A script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    query States and return html
    """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', States=states)


@app.teardown_appcontext
def close_db_session(exception=None):
    """
    close database session after each request
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

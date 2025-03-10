3#!/usr/bin/python3

""" This script starts a Flask web application.
 Routes: / - display “Hello HBNB!”
 Port 5000
 listening on 0.0.0.0
 """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Display “Hello HBNB!” """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

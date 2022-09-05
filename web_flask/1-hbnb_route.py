#!/usr/bin/python3
""" web application hello """
from flask import Flask

web_app = Flask(__name__)


@web_app.route('/', strict_slashes=False)
def hello():
    """ script that starts a Flask web application """
    return 'Hello HBNB!'


@web_app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ display 'HBNB' """
    return 'HBNB'


if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=5000)

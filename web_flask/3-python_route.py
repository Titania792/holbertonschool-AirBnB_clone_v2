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


@web_app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ display 'C {text}' """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@web_app.route('/python', strict_slashes=False)
@web_app.route('/python/(<text>)', strict_slashes=False)
def py_text(text='is cool'):
    """ display 'Python {text}' """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=5000)

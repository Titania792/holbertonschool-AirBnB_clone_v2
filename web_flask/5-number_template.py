#!/usr/bin/python3
""" web application hello """
from flask import Flask, render_template

web_app = Flask(__name__)
web_app.url_map.strict_slashes = False


@web_app.route('/')
def hello():
    """ script that starts a Flask web application """
    return 'Hello HBNB!'


@web_app.route('/hbnb')
def hbnb():
    """ display 'HBNB' """
    return 'HBNB'


@web_app.route('/c/<text>')
def c_text(text):
    """ display 'C {text}' """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@web_app.route('/python')
@web_app.route('/python/<text>')
def py_text(text='is cool'):
    """ display 'Python {text}' """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@web_app.route('/number/<int:n>')
def number(n):
    """ display 'n is a number' only if n is an integer """
    return '{} is a number'.format(n)


@web_app.route('/number_template/<int:n>')
def number(n):
    """ display a HTML page only if n is an integer """
    return render_template(
        '5-number.html',
        num=n
    )


if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=5000)

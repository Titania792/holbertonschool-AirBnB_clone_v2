#!/usr/bin/python3
""" web application """
from flask import Flask, render_template
from models import storage

web_app = Flask(__name__)
web_app.url_map.strict_slashes = False


@web_app.teardown_appcontext
def teardown_db_close(self):
    """ teardown method """
    storage.close()


@web_app.route('/states_list')
def states_list():
    """ states list """
    return render_template(
        '7-states_list.html',
        st_list=storage.all("State").values()
    )


if __name__ == '__main__':
    web_app.run(host='0.0.0.0', port=5000)

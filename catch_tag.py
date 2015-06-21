import json
from flask import Flask
from flask import render_template

application = Flask(__name__)

WOEIDS = None


@application.route('/')
def dashboard_view():
    return render_template('index.html')


def parse_woeids_file():
    with open('supernames.json', 'r') as json_file:
        data = json.load(json_file)
    return data.keys()


if __name__ == '__main__':
    # Parse supernames.json to get a list of woeids.
    WOEIDS = parse_woeids_file()
    application.run()

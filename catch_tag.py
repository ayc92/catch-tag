from flask import Flask
from flask import render_template

application = Flask(__name__)

WOEIDS = None


@application.route('/')
def dashboard_view():
    return render_template('index.html')


if __name__ == '__main__':
    application.run()

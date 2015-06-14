from flask import Flask
from flask import render_template
from flask import request, send_from_directory

app = Flask(__name__)

@app.route('/')
def dashboard_view():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0")

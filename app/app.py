from flask import Flask, render_template
from werkzeug.wrappers import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def get_tweet():
    if request.method == 'GET':
        pass

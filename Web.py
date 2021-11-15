import os
import argparse

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from flask_bootstrap import Bootstrap
#library untuk visualisasi
import numpy as np

app = Flask(__name__, static_folder='static')
bootstrap = Bootstrap(app)
app.config['UPLOAD_FOLDER'] = 'static'

@app.route("/")
def index():
    return render_template('home.html')
    # return "<p>Hello, World!</p>"
    
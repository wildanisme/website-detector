import os
import argparse

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from bs4 import BeautifulSoup as bs
import requests 

from flask_bootstrap import Bootstrap
# library untuk visualisasi
import numpy as np

app = Flask(__name__, static_folder='static')
bootstrap = Bootstrap(app)
app.config['UPLOAD_FOLDER'] = 'static'

# index


@app.route('/', methods=['GET', 'POST'])
def index(domain=None):
    if request.method == 'POST':
        domain = request.form.get('domain')
    return render_template('home.html',
                           site='Home',
                           title='Sistem Pendeteksi Situs Bermuatan Konten Negatif Menggunakan Machine Learning',
                           domain=domain)


# prediksi url yang dimasukkan

@app.route('/prediksi', methods=['POST'])
def predict():
    if request.method == 'POST':
        domain = request.form.get('domain')
        url_input = requests.get(domain)
        scrape = bs(url_input.content, 'html.parser')
        page = scrape
        # api = 'https://website-categorization.whoisxmlapi.com/api/v2?apiKey=at_Uw8qzawOHo1ziJNmCP85ngUozQ9P4&domainName='
        # domain = api+domain
        # return
    return render_template('predict.html',
                           site='Hasil Periksa',
                           title='Sistem Pendeteksi Situs Bermuatan Konten Negatif Menggunakan Machine Learning',
                           domain=domain,
                           page=page)

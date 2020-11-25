#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 11:10:38 2020

@author: ramanan
"""

from flask import Flask, render_template, request
import numpy as np
from tensorflow.keras.models import load_model
import nltk
from nltk.stem.lancaster import LancasterStemmer

app = Flask(__name__)


@app.route('/', methods = ['POST','GET'])
def index():
 return render_template('index.html')
if __name__ == '__main__':
   app.run(debug=True)

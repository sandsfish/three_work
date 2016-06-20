from flask import render_template
from flask import Flask

from networkx.readwrite import json_graph
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime
import requests
import mediacloud
import json
import os
import copy
import cPickle


# from mediacloudlandscape.landscape import *

mc = None

# Berkman Projects Directory
def init():
    berkman_projects = os.environ['BKP']
    api_key = cPickle.load( file( os.path.expanduser( berkman_projects + '/MediaCloud/mediacloud_api_key.pickle' ), 'r' ) )
    mc = mediacloud.api.MediaCloud(api_key)
    print(api_key)

app = Flask(__name__)

@app.route('/')
def index():
    # return '<h1>Python => Three.js</h1>'
    return render_template('index.html')

@app.route('/projects/<string:name>')
def projects(name):
	return render_template(name)

if __name__ == '__main__':
    init()
    app.run(debug=True)
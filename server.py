from flask import render_template
from flask import Flask
from flask import jsonify

#from networkx.readwrite import json_graph
#import networkx as nx
#import pandas as pd
#import numpy as np
#import datetime
#import requests
import mediacloud
import json
import os
import copy
#import cPickle


# from mediacloudlandscape.landscape import *

mc = None
app = Flask(__name__)

# Berkman Projects Directory
def init():
   global mc
   api_key = 'c300df092175a8c3e2c3b5638a3bdbd80214be36581b498d85b1e6d14146748f'
   mc = mediacloud.api.MediaCloud(api_key)
   print(api_key)
   print(mc)
   # print('Calling for data...')
   # top_media = mc.mediaList(timespans_id=1467)
   # top_media = mc.topicMediaList(1477)
   # print(json.dumps(top_media))
   # print('Called')
   #    berkman_projects = os.environ['BKP']
   #    api_key = cPickle.load( file( os.path.expanduser( berkman_projects + '/MediaCloud/mediacloud_api_key.pickle' ), 'r' ) )


# @app.route('/')
# def index():
    # return '<h1>Python => Three.js</h1>'
    # return render_template('index.html')

@app.route('/projects/<path:name>')
def projects(name):
	print 'Name: {0}'.format(name)
	return render_template('/{0}'.format(name))

@app.route('/topic_media/<int:topic_id>')
def topic_media(topic_id):
	# print('Calling for data...')
	top_media = mc.topicMediaList(topic_id)
	# top_media = mc.mediaList(timespans_id=1467)
	# json.dumps(top_media)
	return render_template('mc_topic_media.html', data=top_media)

if __name__ == '__main__':
    init()
    app.run(debug=True)
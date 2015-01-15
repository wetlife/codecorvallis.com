import urllib2
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data/meetup')
def meetup():
    url = 'http://api.meetup.com/2/events?status=upcoming&order=time&limited_events=False&group_urlname=code-corvallis&desc=false&offset=0&photo-host=public&format=json&page=20&fields=&sig_id=28005172&sig=37bee938e0177207d46fb1829369e8b0c5239f50'
    response = urllib2.urlopen(url).read()
    return response
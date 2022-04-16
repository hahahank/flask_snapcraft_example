
from app import app
from flask import Flask, redirect, render_template, request, session, url_for, Response

from . import util

###
# URLs
##
@app.route('/')
def index():
    return render_template('index.html')

###
# APIs
###

@app.route('/system_monitor',methods=['GET', 'POST'])
def data():
    return Response(util.getSystemUsageInfo(), mimetype='json')




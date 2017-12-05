from flask import Flask
from flask import request
from flask import render_template
from flask import send_from_directory
import os
import logging
import gevent.monkey
from time import gmtime, strftime

import sys
sys.path.append('biz')
import realty_handler

app = Flask(__name__,template_folder='template',static_url_path='/ui')
logging.basicConfig(filename=('log/'+strftime("%Y-%m-%d", gmtime())+'.log').encode('utf-8'),level=logging.INFO)


@app.route('/updateRealties')
def updateRealties():
	return realty_handler.updateRealties()

@app.route('/update')
def index():
	root_dir = os.path.dirname(str(os.getcwd()))
	return send_from_directory(os.path.join(root_dir,'app','ui'), 'index.html')


if __name__ == '__main__':
    app.run(debug=True)




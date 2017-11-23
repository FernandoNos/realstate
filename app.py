from flask import Flask
from flask import request
from flask import render_template

import sys
sys.path.append('biz')
import realty_handler

app = Flask(__name__,template_folder='template')


@app.route('/updateRealties')
def updateRealties():
    return realty_handler.updateRealties()

@app.route('/')
def index():
	render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)




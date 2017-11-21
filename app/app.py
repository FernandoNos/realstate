from flask import Flask
import sys
sys.path.append('../biz')
import realty_handler

app = Flask(__name__)

@app.route('/updateRealties')
def index():
    return realty_handler.updateRealties()


if __name__ == '__main__':
    app.run(debug=True)
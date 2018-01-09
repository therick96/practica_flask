# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/p')
def prueba():
    return render_template('prueba.html')


if __name__ == '__main__':
    app.run(port=8080, debug=True)
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request

from flask import render_template #Para renderizar template

app = Flask(__name__) #Objeto



app.run(debug=True, port=8001) #Ejecuta el servidor, puerto default: 5000
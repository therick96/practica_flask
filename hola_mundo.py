# -*- coding: utf-8 -*-

from flask import Flask
from flask import request

from flask import render_template #Para renderizar template

app = Flask(__name__) #Objeto

@app.route('/') #wrap o decorador con la ruta
@app.route('/index.html')
def index():
    web = "Web de Prueba"
    #return "Hola mundo" #Regresa string
    return render_template('index.html', web=web)

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/blog.html')
def blog():
    return render_template('blog.html')

@app.route('/gallery.html')
def gallery():
    return render_template('gallery.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/p')
def pagina_2():
    param = request.args.get('param', 'no hay parametro') #Paso de parametros get
    return param 

@app.route('/p2')
@app.route('/p2/<name>')
@app.route('/p2/<int:num>')
@app.route('/p2/<name>/<int:num>')
def pagina3(name = '', num = ''):
    return '{} {}'.format(name,num) #otra forma de pasar parametros get

app.run(debug=True, port=8001) #Ejecuta el servidor, puerto default: 5000
# -*- coding: utf-8 -*-

import forms

from flask import Flask, request
from flask import render_template #Para renderizar template


app = Flask(__name__) #Objeto

@app.route("/")
def index():
    return render_template("index.html", titulo="Inicio", clase_header='class="alt"')

@app.route("/About", methods = ['GET', 'POST'])
def about():
    form_coment = forms.FormComent(request.form)
    if request.method == 'POST' and form_coment.validate():
        print (form_coment.user.data)
    return render_template("generic.html", titulo="About", clase_body='class="subpage"', form=form_coment)

@app.route("/extras")
def extras():
    return render_template("elements.html", titulo="Extras", clase_body='class="subpage"')

@app.route("/login")
def login():
    return render_template("login.html", titulo="Log In", clase_body='class="subpage"')

@app.route("/SignUp")
def signup():
    return render_template("register.html", titulo="Sign Up", clase_body='class="subpage"')



app.run(debug=True, port=8001) #Ejecuta el servidor, puerto default: 5000
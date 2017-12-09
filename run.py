# -*- coding: utf-8 -*-

import forms
from metodos import sesion #Para validar si esta la sesion abierta

from flask import Flask, request, make_response
from flask import session, redirect, url_for #Para sesiones
from flask import render_template #Para renderizar template
from flask import flash

sesion = sesion()
app = Flask(__name__) #Objeto

app.secret_key = "Secreto"

@app.errorhandler(404) #Para errores
def not_found(e):
    return render_template("404.html"), 404

@app.before_request
def before_request(): #Accion que se ejecuta de primero al abrir pagina
    print request.endpoint # Url de la peticion
    if "user" not in session:
        print "No"

@app.after_request
def after_request(response): # Accion para despues del pedido
    return response #Siempre retorna response


@app.route("/")
def index():
    user = sesion.sesion_abierta()
    #cookie_personalizada = request.cookies.get('CookiePersonalizada', 'No hay Cookie') #Leer Cookie
    #print cookie_personalizada
    #print user
    return render_template("index.html", 
        titulo="Inicio", 
        clase_header='class="alt"', user=user)

@app.route("/About", methods = ['GET', 'POST'])
def about():
    user = sesion.sesion_abierta()
    form_coment = forms.FormComent(request.form)
    if request.method == 'POST' and form_coment.validate():
        print (form_coment.user.data)

    response = make_response( render_template("generic.html", 
        titulo="About", 
        clase_body='class="subpage"', 
        form=form_coment,
        user=user) 
    )
    response.set_cookie('CookiePersonalizada', "Erick") #Crea una cookie
    return response

@app.route("/extras")
def extras():
    user = sesion.sesion_abierta()
    return render_template("elements.html", 
        titulo="Extras", 
        clase_body='class="subpage"',
        user=user)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form_login = forms.login(request.form)
    if request.method == 'POST' and form_login.validate():
        user = session['user'] = form_login.user.data
        mensaje_sucess = 'Hola {}'.format(user)
        flash(mensaje_sucess)
    return render_template("login.html", 
        titulo="Log In", 
        clase_body='class="subpage"', 
        form=form_login) 


@app.route("/SignUp")
def signup():
    form_signUp = forms.signUp(request.form)
    return render_template("register.html", 
        titulo="Sign Up", 
        clase_body='class="subpage"', 
        form=form_signUp)


@app.route("/logout")
def logout(): #Para cerrar la sesion
    sesion.cerrar_sesion()
    return redirect(url_for('login')) #Se coloca la funcion, no la url



app.run(debug=True, port=8001) #Ejecuta el servidor, puerto default: 5000
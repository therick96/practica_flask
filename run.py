# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import forms
from metodos import sesion #Para validar si esta la sesion abierta
from config import Developer_config
from models import User, db

from flask import Flask, request, make_response
from flask import session, redirect, url_for #Para sesiones
from flask import render_template #Para renderizar template
from flask import flash
from flask import g #Variables Globales

sesion = sesion()
app = Flask(__name__) #Objeto
app.config.from_object(Developer_config)


@app.errorhandler(404) #Para errores
def not_found(e):
    return render_template("404.html"), 404

@app.before_request
def before_request(): #Accion que se ejecuta de primero al abrir pagina
    g.user = sesion.sesion_abierta()
    print request.endpoint # Url de la peticion
    if "user" in session and request.endpoint in ['login','SignUp']:
        return redirect(url_for('index'))

@app.after_request
def after_request(response): # Accion para despues del pedido
    return response #Siempre retorna response


@app.route("/")
def index():
    #cookie_personalizada = request.cookies.get('CookiePersonalizada', 'No hay Cookie') #Leer Cookie
    #print cookie_personalizada
    #print user
    return render_template("index.html", 
        titulo="Inicio", 
        clase_header='class="alt"', user=g.user)

@app.route("/About", methods = ['GET', 'POST'])
def about():
    form_coment = forms.FormComent(request.form)
    if request.method == 'POST' and form_coment.validate():
        print (form_coment.user.data)

    response = make_response( render_template("generic.html", 
        titulo="About", 
        clase_body='class="subpage"', 
        form=form_coment,
        user=g.user) 
    )
    response.set_cookie('CookiePersonalizada', "Erick") #Crea una cookie
    return response

@app.route("/extras")
def extras():
    return render_template("elements.html", 
        titulo="Extras", 
        clase_body='class="subpage"',
        user=g.user)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form_login = forms.login(request.form)
    if request.method == 'POST' and form_login.validate():
        mensaje_sucess = None

        username = form_login.user.data
        password = form_login.password.data

        user = User.query.filter_by(username = username).first()
        if user and user.verify_password(password):
            mensaje_sucess = 'Hola {}'.format(user)
            session['user'] = username
            return redirect(url_for("index"))
        else:
            mensaje_sucess = 'Usuario o Contraseña no validos'
            flash(mensaje_sucess)

    return render_template("login.html", 
        titulo="Log In", 
        clase_body='class="subpage"', 
        form=form_login) 


@app.route("/SignUp", methods=['POST','GET'])
def signup():
    form_signUp = forms.signUp(request.form)
    if request.method == 'POST' and form_signUp.validate():
        if form_signUp.password.data == form_signUp.password_repetir.data:
            user = User(form_signUp.user.data, form_signUp.email.data, form_signUp.password.data)

            db.session.add(user)
            db.session.commit()

            flash("Registro Exitoso")
        else:
            flash("Contraseñas Invalidas")

    return render_template("register.html", 
        titulo="Sign Up", 
        clase_body='class="subpage"', 
        form=form_signUp)


@app.route("/logout")
def logout(): #Para cerrar la sesion
    sesion.cerrar_sesion()
    return redirect(url_for('login')) #Se coloca la funcion, no la url


if __name__ == '__main__':
    db.init_app(app) #Configura app al iniciarse

    with app.app_context(): #Para sincronizar la base de datos
        db.create_all() #Crea tablas
    app.run(port=8001) #Ejecuta el servidor, puerto default: 5000
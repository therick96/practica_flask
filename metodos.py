# -*- coding: utf-8 -*-

from flask import session #Para sesiones

class sesion():
    def sesion_abierta(self): #Para validar si esta la sesion abierta
        if "user" in session:
            return session['user']
        else:
            return False

    def cerrar_sesion(self):
        if 'user' in session:
            return session.pop('user')
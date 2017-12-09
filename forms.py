from wtforms import Form
from wtforms import StringField, TextField, HiddenField
from wtforms.fields.html5 import EmailField

from wtforms import validators

class FormComent(Form):
    user = StringField("Usuario",[
            validators.required(message="Y el Usuario?"),
            validators.length(min=4, max=25, message='Usuario no valido')
        ])
    email = EmailField([
            validators.required(message="Y el Email?"),
            validators.Email(message="Email no valido")
        ])
    comment = TextField()
    otro = HiddenField()

class login(Form):
    user = StringField("Usuario", [
            validators.required(message="Y el usuario?")
        ])
    password = StringField("Password", [
            validators.required(message="Y el password?")
        ])


class signUp(Form):
    user = StringField("Usuario", [
            validators.required(message="Y el usuario?")
        ])
    name = StringField("Nombre", [
            validators.required(message="Y el nombre?")
        ])
    email = EmailField("Email", [
            validators.required(message="Y el email?")
        ])
    password = StringField("Password", [
            validators.required(message="Y el password?")
        ])
    password_repetir = StringField("Repetir Password", [
            validators.required(message="Y la validacion del password?")
        ])
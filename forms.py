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
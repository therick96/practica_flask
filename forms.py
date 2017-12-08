from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField

class FormComent(Form):
    user = StringField("Usuario")
    email = EmailField()
    comment = TextField()
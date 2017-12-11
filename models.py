from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(94))
    create_date = db.Column(db.DateTime, default = datetime.now())

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.__create_password(password)

    def __create_password(self, password):
        return generate_password_hash(password)
import os

class config(object):
    SECRET_KEY = "Secreto"

class Developer_config(config):
    DEBUG = True
    #Necesario para mysql: apt-get install mysql-server mysql-common mysql-client 
    # Flask-SQLAlchemy
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/Prueba_flask'
    #ALTER USER db_username PASSWORD 'new_password'; para psql
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/prueba_flask'
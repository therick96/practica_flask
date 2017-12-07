from flask import Flask

app = Flask(__name__) #Objeto

@app.route('/') #wrap o decorador con la ruta
def index():
    return "Hola mundo" #Regresa string

app.run() #Ejecuta el servidor, puerto default: 5000
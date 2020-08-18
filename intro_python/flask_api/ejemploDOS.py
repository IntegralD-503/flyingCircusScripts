#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask, redirect, url_for

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/")
def hola():
   return "<h1>....main page</h1>"
#app.add_url_rule("/hola", "hola", hola)
@app.route("/admin")
def hola_admin():
    return "hola admin"

@app.route("/hola/<nombre>")
def hola_nombre(nombre):
    return f"<h1>hola {nombre}</h1>"

@app.route("/guest/<viajero>")
def hola_viajero(viajero):
    return f"<h2>hola {viajero}</h2>"

@app.route("/user/<nombre>")
def hola_user(nombre):
    if nombre == "admin":
        return redirect(url_for("hola_admin"))
    else:
        return redirect(url_for("hola_viajero",viajero = nombre))

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE


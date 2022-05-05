import os
from flask import Flask, render_template, abort, request
import json
app = Flask(__name__)

with open("MSX.json") as fich:
    todatos=json.load(fich)

#Página Inicio
@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("inicio.html")

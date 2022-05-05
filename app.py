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

#Página Juegos
@app.route('/juegos',methods=["GET","POST"])
def juegos():
	categorias=[]
	for i in todatos:
		categorias.append(str(i["categoria"]))
	categorias=list(set(categorias))
	if request.method=="GET":
		return render_template("juegos.html",categorias=categorias)
	else:
		try:
			cadena=request.form.get("name")
		except:
			abort(404)
		categoria=request.form.get("cat")
		listajuegos=[]
		listaidentificadores=[]
		listadesarrolladores=[]
		for dat in todatos:
			if cadena in str(dat["nombre"]) and categoria == str(dat["categoria"]):
				listajuegos.append(str(dat["nombre"]))
				listaidentificadores.append(str(dat["id"]))
				listadesarrolladores.append(str(dat["desarrollador"]))
				todo=zip(listajuegos,listadesarrolladores,listaidentificadores,categorias)
			elif cadena == "" and categoria == "":
				listajuegos.append(str(dat["nombre"]))
			elif cadena in str(dat["nombre"]) and categoria == "Todos":
				listajuegos.append(str(dat["nombre"]))
				listadesarrolladores.append(str(dat["desarrollador"]))
				listaidentificadores.append(str(dat["id"]))
				todo=zip(listajuegos,listadesarrolladores,listaidentificadores,categorias)

		return render_template("juegos.html",juegos=todo,cadena=cadena,categorias=categorias,categoria=categoria)

#Página de detalles sobre un juego
@app.route('/juego/<int:identificador>', methods=["GET","POST"])
def detallejuego(identificador):
	for a in todatos:
		if a["id"] == identificador:
			return render_template("detallejuego.html",detalle=a)
	abort(404)

port=os.environ["PORT"]
app.run('0.0.0.0', int(port), debug=False)

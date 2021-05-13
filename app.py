from flask import Flask, render_template,abort,json
import os
app = Flask(__name__)	

f = open('books.json',)

datos = json.load(f)

@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("inicio.html",lista_libros=datos)

@app.route('/libros/<isbn>')
def libros(isbn):
    for libro in datos:
        if libro.get("isbn")==isbn:
            return render_template("libros.html",contenido=libro)
    abort(404)

@app.route('/categorias/<tipo>')
def categoria(tipo):
    listacategorias=[]
    for cate in datos:
        for lista in cate.get("categories"):
            if lista==tipo:
                listacategorias.append(cate)
    return render_template("categorias.html",categoria=tipo,lista_categorias=listacategorias,lista_libros=datos)

port=os.environ["PORT"]
app.run('0.0.0.0',int(port),debug=True)

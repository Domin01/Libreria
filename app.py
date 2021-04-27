from flask import Flask, render_template,abort,json
app = Flask(__name__)	

f = open('books.json',)

datos = json.load(f)

@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("inicio.html",lista_libros=datos)

@app.route('/libros/<isbn>')
def libros(isbn):
    for libro in datos:
        if libro["isbn"]==isbn:
            return render_template("libros.html",contenido=libro)
    abort(404)


app.run("0.0.0.0",8000,debug=True)


#Página detalle del libro. La ruta será /libro/<isbn>, que mostrará un título con el nombre del libro, una imagen del libro 
#(campo thumbnailUrl) y la siguiente información del libro: Número de páginas, descripción, autores y categorías.
#Si el ISBN no existe se devolverá un error 404.
#Si el valor del campo status es igual a MEAP mostraremos un mensaje que diga "ESTE LIBRO NO SE HA PUBLICADO" 
#(usar un if dentro de la plantilla).

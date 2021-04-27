from flask import Flask, render_template,abort,json
app = Flask(__name__)	

f = open('books.json',)

datos = json.load(f)

@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("inicio.html",lista_libros=datos)

@app.route('/libros/<int:isbn>')
def libros(isbn):
	return render_template("libros.html",isbn=codigo)
	
app.run("0.0.0.0",8000,debug=True)


#La aplicación nos va a permitir mostrar información de libros. 

#Esa información está guardada en el fichero books.json.
#La página principal debe mostrar una página donde ponga vuestro nombre, un título con la palabra "Biblioteca" y una 
#lista de enlaces donde se vean los nombres de todos los libros y que nos lleve a una ruta del tipo /libro/<isbn>. 
#Es decir si el libro 1 tienes ISBN 1933988673 el enlace nos llevara a la ruta /libro/1933988673.


#Página detalle del libro. La ruta será /libro/<isbn>, que mostrará un título con el nombre del libro, una imagen del libro 
#(campo thumbnailUrl) y la siguiente información del libro: Número de páginas, descripción, autores y categorías.
#Si el ISBN no existe se devolverá un error 404.
#Si el valor del campo status es igual a MEAP mostraremos un mensaje que diga "ESTE LIBRO NO SE HA PUBLICADO" 
#(usar un if dentro de la plantilla).

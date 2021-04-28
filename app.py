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




app.run("0.0.0.0",8000,debug=True)


#Posible mejora (no es obligatorio, pero estaría muy bien que lo hagáis)

#Cuando se muestra el detalle de un libro y se muestran las categorías, estás son un enlace a la ruta /categoria/<categoria>. 
#Por ejemplo, si el primer libro tiene una categoría  Mobile, al pulsar sobre el enlace nos lleva a la página /categoria/Mobile

#Libros por categoría: Esta página está en la ruta /categoria/<categoria>: Es muy similar a la página principal, 
#pero sólo muestra la los libros de esa ccategoría. Además debe a aprecer un título con la categoría.
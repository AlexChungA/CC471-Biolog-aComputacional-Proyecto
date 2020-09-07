from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome

app = Flask(__name__) 
bootstrap = Bootstrap(app)
fa = FontAwesome(app)

@app.route("/")
def index():
    return render_template("index.html",title="INICIO")

@app.route("/Analisis/Proteina")
def proteina():
    return render_template("analisis_prot.html",title="ANALISIS PROTEINAS")

#manejando rutas con variables dadas
@app.route("/Analisis/Arbol")
def arbol():
    return render_template("analisis_arbol.html",title="ANÁLISIS ARBOL FILOGENÉTICO")

@app.route("/About")
def about():
    return render_template("about.html",title="ACERCA DE")


if __name__ == "__main__":
    app.run(debug=False,port=3000)   
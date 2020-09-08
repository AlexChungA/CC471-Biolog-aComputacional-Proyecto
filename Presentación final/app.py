from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
import formsFunc as ff
import bioFunc as bf
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_key'
bootstrap = Bootstrap(app)


@app.route("/")
def index():
    return render_template("index.html", title="INICIO")


@app.route("/Analisis", methods=('GET', 'POST'))
@app.route("/Analisis/Gen", methods=('GET', 'POST'))
def gen():
    form_g = ff.gen_form()
    lista = bf.importar_genes("Chikunguya")
    lista_homologos = []
    form_g.gen_list.choices = lista
    if form_g.validate_on_submit():
        flash('Gen escogido = %s' % (form_g.gen_list.data))
        indice = int(form_g.gen_list.data)
        file_homologo = form_g.gen_list.data
        file_homologo += '.fasta'
        lista_homologos = bf.importar_homologos_G(file_homologo)
        info = bf.getSeq_G("Chikunguya", lista[indice-1][1])
        return render_template('analisis_gen.html', title='Gen', form=form_g, lista=lista_homologos, info=info)

    return render_template("analisis_gen.html", title="ANÁLISIS GENES", form=form_g)


@app.route("/Analisis/Proteina", methods=('GET', 'POST'))
def proteina():
    form_p = ff.protein_form()
    lista = bf.importar_proteinas("Chikunguya")
    lista_homologos = []
    form_p.protein_list.choices = lista
    if form_p.validate_on_submit():
        flash('Proteina escogida = %s' % (form_p.protein_list.data))
        indice = int(form_p.protein_list.data)
        file_homologo = form_p.protein_list.data
        file_homologo += '.fasta'
        lista_homologos = bf.importar_homologos_P(file_homologo)
        info = bf.getSeq_P("Chikunguya", lista[indice-1][1])
        return render_template('analisis_prot.html', title='Proteina', form=form_p, lista=lista_homologos, info=info)
    return render_template("analisis_prot.html", title="ANALISIS PROTEINAS", form=form_p)

# manejando rutas con variables dadas


@app.route("/Analisis/Arbol", methods=('GET', 'POST'))
def arbol():
    form_t = ff.tree_form()
    lista = bf.importar_genes("Chikunguya")
    form_t.tree_list.choices = lista
    if form_t.validate_on_submit():
        flash('ID: %s' % (form_t.tree_list.data))
        indice = form_t.tree_list.data
        path_arbol_num = './static/docs/Homologos/Nucleotidos'+form_t.tree_list.data
        comando = 'clustalw ' + path_arbol_num + '.fasta'
        os.system(comando)
        bf.generar_arbol(path_arbol_num + '.aln', indice)
        info = list(open('./static/docs/Informacion/'+indice+'.txt', 'r'))[1]
        return render_template('analisis_arbol.html', title='Arbol', form=form_t, indice=indice, info=info)
    return render_template("analisis_arbol.html", title="ANÁLISIS ARBOL FILOGENÉTICO", form=form_t)


@app.route("/About")
def about():
    return render_template("about.html", title="ACERCA DE")


if __name__ == "__main__":
    app.run(debug=False, port=3000)

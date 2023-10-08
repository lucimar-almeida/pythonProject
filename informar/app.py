from flask import Flask, render_template

app = Flask(__name__)


# criar a primeira pagina do site

# route -> lucimaralmeidadasilva.com/usuarios
# função -> o que vc quer exibir na pagina
# template
@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/contatos")
def contatos():
    return render_template("contatos.html")


@app.route("/usuario/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)


# colocar no ar
if __name__ == "__main__":
    app.run(debug=True)

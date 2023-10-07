from flask import Flask

app = Flask(__name__)

#criar a primeira pagina do site

#route -> lucimaralmeidadasilva.com/usuarios
#função -> o que vc quer exibir na pagina

@app.route("/")
def homepage():
    return "Esse é meu primeiro site"







#colocar no ar

app.run(debug=True)
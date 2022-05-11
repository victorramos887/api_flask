# AULA 2 CRIANDO CONFIGURAÇÃO DE ROTAS;

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "index"

def teste():
    return "<p>Análise dos setores.</p>"
app.add_url_rule('/teste', 'teste', teste)


# INÍCIANDO O APP

if __name__ == '__main__':
    app.run(debug=True)
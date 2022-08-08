from flask import Flask, Response, request
from flask_sqlalchemy import *
from psycopg2 import connect
import json


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/gemini'


db = SQLAlchemy(app)

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(100))

    def to_json(self):
        return {"id":self.id, "nome":self.nome, "email":self.email}

def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {nome_do_conteudo:conteudo}
    if(mensagem):
        body['mensagem'] = mensagem
    return Response(json.dumps(body), status = status, mimetype="application/json")



#SELECIONAR TUDO
@app.route('/usuarios', methods=['GET'])
def seleciona_usuarios():

    usuarios_objetos = Usuario.query.all()
    usuario_json = [usuario.to_json() for usuario in usuarios_objetos]
    print(usuario_json)
    return gera_response(200,"usuario", usuario_json, 'Retorno Response')

#http://127.0.0.1:5000/usuarios
app.run(debug=True)
#SELECIONAR UM
#CADASTRAR
#ATUALIZAR
#DELETAR



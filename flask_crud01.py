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
    usuarios_json = [usuario.to_json() for usuario in usuarios_objetos]
    return gera_response(200,"usuarios", usuarios_json, 'Retorno Response')


@app.route('/usuario/<id>', methods=['GET'])
def seleciona_usuario(id):

    usuario_objeto = Usuario.query.filter_by(id=id).first()
    usuario_json = usuario_objeto.to_json()
    print(usuario_json)
    return gera_response(200, "usuario", usuario_json, 'Retorno Response')


#http://127.0.0.1:5000/usuarios

#SELECIONAR INDIVIDUALMENTE

#CADASTRAR
@app.route('/usuario', methods=['POST'])
def criar_usuario():
    body = request.get_json()

    #Validar se veio os parametros para
    try:
        usuario = Usuario(nome = body['nome'], email = body['email'])
        db.session.add(usuario)
        db.session.commit()
        return gera_response(201, 'usuario', usuario.to_json(), 'Criado com sucesso')
    except Exception as e:
        print(e)
        return gera_response(400,"usuario", {}, "Erro ao cadastrar")

#ATUALIZAR
@app.route('/usuario/<id>', methods=['PUT'])
def atualizar_usuario(id):
    usuario_objeto = Usuario.query.filter_by(id=id).first()
    body = request.get_json()

    try:
        if('nome' in body):
            usuario_objeto.nome = body['nome']
        if('email' in body):
            usuario_objeto.email = body['email']
        db.session.add(usuario_objeto)
        db.session.commit()
        return gera_response(200, "usuario", usuario_objeto.to_json(), 'Atualizado com sucesso')
    except Exception as e:
        print('ERRO', e)
        return gera_response(400, "usuario", {}, 'Erro ao atualizar usuario')

#DELETAR


@app.route('/usuario/<id>', methods=["DELETE"])
def deletar_usuario(id):
    usuario_objeto = Usuario.query.filter_by(id = id).first()

    try:
        db.session.delete(usuario_objeto)
        db.session.commit()
        return gera_response(200, 'usuario', usuario_objeto.to_json(), 'Deletado com sucesso')
    except Exception as e:
        print('ERRO', e)
        return gera_response(400, 'usuario', {}, 'Erro ao deletar')

app.run(debug=True)
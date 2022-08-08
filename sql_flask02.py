from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

#ESPECIFICO DO POSTGRESQL
from sqlalchemy_utils import database_exists, create_database

from pprint import pprint



# CRIANDO BANCO DE DADOS
engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/testes.db', echo = True)
Session = sessionmaker(bind = engine)
session = Session()

#CRIANDO DATA BASE SE NÃO EXISTIR
if not database_exists(engine.url):
    create_database(engine.url)

Base = declarative_base()
class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key = True)
    nome = Column(String)
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship('Pessoa')

    def __repr__(self):
        return f"Produto(nome = {self.nome}, pessoa_id = {self.pessoa_id})"

class Pessoa(Base):
    __tablename__ = 'pessoas'

    id = Column(Integer, primary_key = True)
    nome = Column(String)
    idade = Column(Integer)
    produtos = relationship(Produto, backref='pessoas')

    def __repr__(self):
        return f"Pessoa(nome={self.nome}, idade = {self.idade}, produtos = {self.produtos})"


Base.metadata.create_all(engine)

p1 = Pessoa(nome = 'Fausto', idade = 24)
p2 = Pessoa(nome = 'Fabio', idade = 28)
p3 = Pessoa(nome = 'Arnaldo', idade = 30)
p4 = Pessoa(nome = 'Fernando', idade = 19)

pd1 = Produto(nome = 'Livro', pessoa = p1)
pd2 = Produto(nome = 'CD', pessoa = p1)
session.add_all([p1, p2, p3, p4, pd1, pd2])
#session.commit()
session.flush()

session.query(Produto).filter_by(nome = 'CD').filter(Pessoa.nome=='Fausto').all()
session.query(Pessoa).filter_by(nome='Fausto').all()

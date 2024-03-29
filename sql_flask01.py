from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
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

class Pessoa(Base):
    __tablename__ = 'pessoas'

    id = Column(Integer, primary_key = True)
    nome = Column(String)
    idade = Column(Integer)

    def __repr__(self):
        return f"Pessoa(nome={self.nome}, idade = {self.idade})"

Base.metadata.create_all(engine)

p1 = Pessoa(nome = 'Fausto', idade = 24)
p2 = Pessoa(nome = 'Fabio', idade = 28)
p3 = Pessoa(nome = 'Arnaldo', idade = 30)
p4 = Pessoa(nome = 'Fernando', idade = 19)

session.add_all([p1, p2, p3, p4])
session.flush()


pprint(session.query(Pessoa).first())
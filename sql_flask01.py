from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# CRIANDO BANCO DE DADOS


engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/testes.db', echo = True)
Session = sessionmaker(bind = engine)
session = Session()

Base = declarative_base()


class Pessoa(Base):
    __tablename__ = 'pessoas'

    id = Column(Integer, primary_key = True)


Base.metadata.create_all(engine)
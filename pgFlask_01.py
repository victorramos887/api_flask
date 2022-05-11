from flask import Flask, render_template
import psycopg2 as pg
import psycopg2.extras

#CRIANDO O APP FLASK
app = Flask(__name__)

#ATRIBUTOS PARA CONEXÃO DO BANCO
DB_HOST = '192.168.1.199'
DB_NAME = 'gemini'
DB_USER = 'postgres'
DB_PASS = 'postgres'

#CONECTANDO NO BANCO

conn = pg.connect(dbname = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST)

@app.route('/')
def index()


if __name__ == "__main__":
    app.run(debug=True)
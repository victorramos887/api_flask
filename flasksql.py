from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import psycopg2 as pg

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URL'] = 'postgresql://postgres:postgres@192.168.1.199/gemini'
db = SQLAlchemy(app)


def conectar():
    conn = pg.connect(database = 'gemini', host = '192.168.1.199', password = 'postgres', user = 'postgres')
    return conn




@app.route('/')
def index():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM main.datalogger")

    datalogger = cur.fetchall()
    cur.close()
    conn.close()
    return 'str(type(datalogger))'


if __name__ == "__main__":
    app.run(debug=True)
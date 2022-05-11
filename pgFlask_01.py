from flask import Flask, render_template, jsonify
import psycopg2 as pg
import psycopg2.extras
import json
import pandas as pd
from datetime import datetime



#CRIANDO O APP FLASK
app = Flask(__name__)

#ATRIBUTOS PARA CONEXÃO DO BANCO
DB_HOST = '192.168.1.199'
DB_NAME = 'gemini'
DB_USER = 'postgres'
DB_PASS = 'postgres'

#CONECTANDO NO BANCO

conn = pg.connect(dbname = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST)

@app.route('/<valor>')
def index(valor):

    s = """INSERT INTO main.datalogger VALUES (DEFAULT, '14-04-2022', '14-04-2022 10:45:00', 25, 15, 16, 25, 21)"""
    leitura = {
        "Id":valor[:3],
        "Data": f'{valor[3:5]}/{valor[5:7]}/{valor[7:9]}',
        "Hora": f'{valor[9:11]}:{valor[11:13]}',
        "Temperatura": f'{valor[13:15]}',
        "Sensor1": f'{valor[15:20]}',
        "Sensor2":f'{valor[20:25]}',
        "Sensor3":f'{valor[25:30]}',
        "ControledePulsos":f'{valor[30:]}',
        "DataHora": f"{valor[3:5]}/{valor[5:7]}/{valor[7:9]} {valor[9:11]}:{valor[11:13]}"
               }

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    print(leitura['DataHora'])
    cur.execute(s)
    conn.commit()

    return "Salvo"


if __name__ == "__main__":
    app.run(debug=True)
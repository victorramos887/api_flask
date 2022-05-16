from mailbox import NotEmptyError
import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__, static_folder='public')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///gemini'

db = SQLAlchemy(app)

class Datalogger(db.Model):
    id = db.Column('id', db.Integer, primary_key = True, autoincrement = True)
    nome = db.Column(db.String(150))
    idade = db.Column(db.Integer)

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


db.create_all()



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
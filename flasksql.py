from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URL'] = 'postgresql://postgres:postgres@192.168.1.199/gemini'
db = SQLAlchemy(app)

import psycopg2 as pg

from flask import Flask, render_template


app = Flask(__name__, template_folder='template')

def get_db_connection():
    return pg.connect(host = 'localhost', database = 'estudos', user = 'postgres', password = 'postgres')

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM books')
    books = cur.fetchall()
    cur.close()
    conn.close()

    return render_template('index.html', books=books)


if __name__ == '__main__':
    app.run(debug=True)
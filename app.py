from flask import Flask, render_template, request, url_for, redirect, redirect
import psycopg2

app = Flask(__name__, template_folder='template')

def get_connect_database():
    return psycopg2.connect(host = 'localhost', database = 'estudos', user = 'postgres', password = 'postgres')

@app.route('/')
def index():
    conn = get_connect_database()
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', books= books)

@app.route('/insertBooks', methods=['GET', 'POST'])
def insertBooks():

    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        pages_num = request.form['pages_num']
        review = request.form['review']

        conn = get_connect_database()
        cur = conn.cursor()
        cur.execute('INSERT INTO books (title, author, pages_num, review)'
                    'VALUES (%s, %s, %s, %s)', (title, author, pages_num, review))

        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=True)
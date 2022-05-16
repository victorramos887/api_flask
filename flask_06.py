from difflib import restore
from flask import Flask, request

app = Flask(__name__, static_folder='public')

@app.route('/add/<leitura>', methods= ['GET','POST'])   
def add(leitura):
    if request.method == 'POST':
        return f'Valor post == {request.form}'
    return f'{leitura}'

if __name__ == "__main__":
    app.run(debug=True)
from crypt import methods
from flask import Flask, request

app = Flask(__name__, static_folder='public')

@app.route('/add', methods= ['GET','POST'])   
def add():
    if request.method == 'POST':
        return 'POST OKK'
    else:
        return 'GET OKK'


if __name__ == "__main__":
    app.run(debug=True)
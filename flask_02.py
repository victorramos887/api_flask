# AULA 2 - URL DINÂMICA

from flask import Flask

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<nome>')
def hello(nome = ""):
    return f"<h1>Hello {nome}</h1>"


@app.route('/blog/')
@app.route('/blog/<int:postID>')


def blog(postID = -1):
    if postID >= 0:
        return f"Blog info {postID}"
    else:
        return "Blog todo"

if __name__ == "__main__":
    app.run(debug=True)
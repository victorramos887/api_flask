from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return "API NO AR"

@app.route('/primeiraroute', methods = ['POST', 'GET'])
def primeiraroute():
    #print(request.method, request.args)
    t1 = request.args.to_dict()
    t2 = dict(request.args)

    print('-------------------- ANÁLISE DAS INFORMAÇÕES ------------------------')
    print(t2)
    return json.dumps([t1['nome'], t2['idade'], t1['analise']])

if __name__ == '__main__':
    app.run(debug=True)
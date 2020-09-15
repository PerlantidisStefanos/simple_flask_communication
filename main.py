#main.py
from readFromSql import getFromSql
import pandas as pd
from flask import Flask, Response
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
@cross_origin()
def hello():
    return "Hello World! My name is Stefanos!"

@app.route('/get', methods=['GET'])
@cross_origin()
def getData():
    return Response(getFromSql('PersonData').to_json(orient="records"),
     mimetype='application/json')

if __name__ == '__main__':
    app.run()
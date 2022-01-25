from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from random import randrange
from lorem_text import lorem


app= Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def generate_data(n):
    data = []
    for i in range(0, n):
        data.append(dict(name=lorem.sentence().split(' ')[0], lastname=lorem.sentence().split(' ')[0], age=randrange(100)))
    return data


@app.route("/data", methods=["GET"])
@cross_origin()
def hello_world():
    n = request.args.get('n')
    return jsonify(generate_data(int(n)))


if __name__=='__main__':
    app.run(debug=True)
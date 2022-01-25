from flask import Flask, jsonify, request
from random import randrange
from lorem_text import lorem


app= Flask(__name__)

return_data = []
for i in range(0, 10):
    return_data.append(dict(name=lorem.sentence().split(' ')[0], lastname=lorem.sentence().split(' ')[0], age=randrange(100)))

@app.route("/hello", methods=["GET"])
def hello_world():
    # data = request.get_json()
    # name = request.args.get('name')
    # return jsonify("Hello " + name + " !")
    return jsonify(return_data)


if __name__=='__main__':
    app.run(debug=True)
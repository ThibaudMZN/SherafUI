from api.samples.anything import SherafDBManager
from api.samples.anything import TodoItem
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

db = SherafDBManager()

@app.route("/data", methods=["GET"])
@cross_origin()
def get_all_data():
    # n = request.args.get('n')
    return jsonify(db.get_data_from_type(TodoItem))


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client.stem_learning

@app.route('/api/interactions', methods=['GET'])
def get_interactions():
    data = list(db.student_interactions.find({}, {'_id': 0}))
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

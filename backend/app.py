from flask import Flask, render_template_string, jsonify
import os
from pymongo import MongoClient
 
app = Flask(__name__, static_folder='frontend', template_folder='frontend')
 
MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/mydatabase")
client = MongoClient(MONGO_URI)
db = client.get_default_database()  # uses DB from URI or default
 
@app.route("/")
def home():
    # serve static HTML file
    return app.send_static_file("index.html")
 
@app.route("/items")
def items():
    # simple example: read collection 'items'
    items = list(db.items.find({}, {"_id": 0}))
    return jsonify(items)
 
@app.route("/add-sample")
def add_sample():
    db.items.insert_one({"name": "sample", "value": 1})
    return "added", 201
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

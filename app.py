
from flask import Flask, request, jsonify
from pymongo import MongoClient
import uuid

app = Flask(__name__)

# MongoDB connection setup
client = MongoClient('mongodb://root:password@ecp-cd-mongo-headless.lcm-mongo.svc.cluster.local:27017/?replicaSet=rs0')
db = client['test']
collection = db['product']

@app.route('/product/<id>', methods=['GET'])
def get_product(id):
    # Query MongoDB for the product with the given product_id
    
    for x in collection.find({ "product_no": id}):
        x['_id'] = str(x['_id']) 
        print(x)

    if x:
        del x["_id"]
        return jsonify(x), 200
    else:
        # If the product is not found, return an error message
        return jsonify({'status': 'failure', 'message': 'Product not found'}), 404


@app.route('/product', methods=['POST'])
def add_product():
    # Get data from request
    data = request.json
    data["product_no"] = str(uuid.uuid4())

    # Insert the data into MongoDB
    inserted_product = collection.insert_one(data)

    # Return the inserted document ID
    return jsonify({'status': 'success', 'message': 'Product added', 'product_no': data["product_no"]}), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    #app.run(debug=True)


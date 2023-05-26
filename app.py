import os
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app

app = Flask(__name__)

# Instatiate a Firestore client
cred = credentials.Certificate('./serviceaccount.json')
initialize_app(cred)
db = firestore.client()
wayang_ref = db.collection('wayang_detail')

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

# Create a route for reading data detail wayang
@app.route('/wayang', methods=['POST'])
def read():
    # Picking parameter from URL to filter must Integer
    field_id = request.form.get('field_id')
    
    try:
        field_id = int(field_id)
    except ValueError:
        return jsonify({'message': 'Parameter must Integer'})
    
    if field_id:
        query = wayang_ref.where('id', '==', field_id).limit(1)
        docs = query.stream()

        result = []
        for doc in docs:
            result = doc.to_dict()
            break

        if result:
            return jsonify(result)
        else:
            return jsonify({'message': 'Document not found'})
    else :
        return jsonify({'message': 'Parameter not found'})

# Create a route for reading data list(all) wayang
@app.route('/wayanglist', methods=['POST'])
def read_all():
    docs = wayang_ref.stream()

    results = []
    for doc in docs:
        data = doc.to_dict()
        data['gambar'] = data['gambar'][0]
        del data['detail']
        results.append(data)

    return jsonify(results)

if __name__ =='__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
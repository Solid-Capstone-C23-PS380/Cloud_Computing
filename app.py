import os
from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app

app = Flask(__name__)

# Instatiate a Firestore client
cred = credentials.Certificate('serviceaccount.json')
initialize_app(cred)
db = firestore.client()
wayang_ref = db.collection('wayang_detail')

@app.route('/list', methods=['GET'])
def read():
    # Picking parameter from URL to filter
    field_names = request.form.get('field_name')
    if field_names:
        query = wayang_ref.where('nama', '==', field_names).limit(1)
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


if __name__ =='__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8081)))
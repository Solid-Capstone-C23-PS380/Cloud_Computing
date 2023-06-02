import os
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app
from google.cloud import storage
import tempfile

app = Flask(__name__)

# Instatiate a Firestore client
cred = credentials.Certificate('./serviceaccountfb.json')
initialize_app(cred)
db = firestore.client()
wayang_ref = db.collection('wayang_detail')
video_ref = db.collection('video_pementasan')
event_ref = db.collection('wayang_event')
ticket_ref = db.collection('ticket_event')

# Inistantiate a Google Cloud Storage client
storage_client = storage.Client.from_service_account_json('./serviceaccountgcs.json')
bucket_name = 'wayang-storage'
bucket = storage_client.get_bucket(bucket_name)

# Initialize CORS for Flask
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Cache-Control'
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
    if docs:
        results = []
        for doc in docs:
            data = doc.to_dict()
            results.append(data)
        return jsonify(results)
    else:
        return jsonify({'message': 'Document not found'})

# Create a route for reading all data video
@app.route('/videolist', methods=['POST'])
def read_video():
    docs = video_ref.stream()
    if docs:
        results = []
        for doc in docs:
            data = doc.to_dict()
            results.append(data)
        return jsonify(results)
    else:
        return jsonify({'message': 'Document not found'})

# Create a route for reading one data video
@app.route('/video', methods=['POST'])
def read_one_video():
    # Picking parameter from URL to filter must Integer
    field_id = request.form.get('field_id')
    
    try:
        field_id = int(field_id)
    except ValueError:
        return jsonify({'message': 'Parameter must Integer'})
    
    if field_id:
        query = video_ref.where('id', '==', field_id).limit(1)
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
        

# Create a route for read all event data
@app.route('/eventlist', methods=['POST'])
def read_event():
    docs = event_ref.stream()
    if docs:
        results = []
        for doc in docs:
            data = doc.to_dict()
            results.append(data)
        return jsonify(results)
    else:
        return jsonify({'message': 'Document not found'})

# Create a route for read one event data
@app.route('/event', methods=['POST'])
def read_one_event():
    # Picking parameter from URL to filter must Integer
    field_id = request.form.get('field_id')
    
    try:
        field_id = int(field_id)
    except ValueError:
        return jsonify({'message': 'Parameter must Integer'})
    
    if field_id:
        query = event_ref.where('id', '==', field_id).limit(1)
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


# Update a route for update data event / buying tickets
@app.route('/ticket_event', methods=['POST'])
def update_event():
    # Picking parameter from URL to filter must Integer and more requirements each field
    event_id = request.form.get('event_id')
    if event_id == '':
        return jsonify({'message': 'Event id is required'})
    event_id = int(event_id)
    
    tickets_bought = request.form.get('tickets_bought')
    if tickets_bought == '':
        return jsonify({'message': 'Tickets bought is required'})
    tickets_bought = int(tickets_bought)

    name = request.form.get('name')
    if name == '':
        return jsonify({'message': 'Name is required'})
    
    email = request.form.get('email')
    if email == '':
        return jsonify({'message': 'Email is required'})
    
    payment_method = request.form.get('payment_method')
    if payment_method == '':
        return jsonify({'message': 'Payment method is required'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No file selected'})
    
    # Save temp file to server
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    file.save(temp_file.name)

    # update ticket_event collection
    if event_id:
        query = event_ref.where('id', '==', event_id).limit(1)
        docs = query.stream()
        result = []
        for doc in docs:
            result = doc.to_dict()
            if result['ticket_count'] == 0:
                return jsonify({'message': 'Tickets sold out'})
            if result['ticket_count'] < tickets_bought:
                return jsonify({'message': 'Not enough tickets'})
            
            # Save temp file to Google Cloud Storage
            blob = bucket.blob('pic/receipt/' + file.filename)
            blob.upload_from_filename(temp_file.name)
            # get public url for shown image
            image_url = blob.public_url

            result_count = result['price'] * tickets_bought

            data = {
                'event_id': event_id,
                'name': name,
                'email': email,
                'method': payment_method,
                'payment_picture': image_url,
                'total_count': result_count,
                'ticket_bought': tickets_bought
            }

            result['ticket_count'] = result['ticket_count'] - tickets_bought
            doc.reference.update({'ticket_count': result['ticket_count']})
            
            ticket_doc_ref = ticket_ref.document()
            ticket_doc_ref.set(data)
            response = {
                'message': 'success',
                'data': data
            }
            break
        if result:
            temp_file.close()
            return jsonify(response)
        else:
            return jsonify({'message': 'Document not found'})
    else :
        return jsonify({'message': 'Parameter not found'})
    
# Upload a photo profile to Google Cloud Storage
@app.route('/upload_profile', methods=['POST'])
def upload_file():
    file = request.files['file']
    
    uid = request.form['uid']
    if uid == '':
        return jsonify({'message': 'No uid selected'})

    # Save temp file to server and rename formatted file
    new_filename = uid + '.jpg'
    file.filename = new_filename
    temp_file1 = tempfile.NamedTemporaryFile(delete=False)
    file.save(temp_file1.name)
    if file.filename == '':
        return jsonify({'message': 'No file selected'})
    
    blob = bucket.blob('pic/profile/' + file.filename)
    blob.cache_control = 'no-cache'
    blob.upload_from_filename(temp_file1.name)
    # get public url for shown image
    image_url = blob.public_url
    response = {
        'message': 'success',
        'image_url': image_url
    }
    temp_file1.close()   
    return jsonify(response)
   

if __name__ =='__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
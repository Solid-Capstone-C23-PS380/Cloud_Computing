# Import Packages
import os
from flask import Flask, request, jsonify, json, make_response
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import tensorflow as tf
from tensorflow import keras
from google.cloud import storage
import tempfile

# Flask App
app = Flask(__name__)

# Declare Model and Class
labels = ['Abimanyu', 'Antasena', 'Bagong', 'Bima', 'Gareng', 'Gatot Kaca', 'Hanoman', 'Krisna', 'Petruk', 'Semar']
model = load_model("./Model.h5")

# Cors Handling if using web
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

# backend Code for Prediction using image processing
@app.route("/predict", methods=['POST'])
def predict():
    if 'file' not in request.files:
        return 'No file part in the request'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    # Save file to temp folder
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    file.save(temp_file.name)
    
    # Predict Image
    image = keras.preprocessing.image.load_img(temp_file.name, target_size=(150, 150))
    x = keras.preprocessing.image.img_to_array(image)
    x = x / 255.0
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])

    pred = model.predict(images)
    preds = labels[np.argmax(pred)]
    
    # Delete temp file
    temp_file.close()

    # return prediction
    return jsonify(
        {
            "result": preds
        })

if __name__ =='__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
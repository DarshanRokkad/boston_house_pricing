from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np 
import pandas as pd
import pickle

application = Flask(__name__)
app = application

# load the models
scaler = pickle.load(open('models/scaler_object.pkl', 'rb'))
model = pickle.load(open('models/regressor_model.pkl', 'rb'))

@app.route('/')
def home_page():
    return render_template('home.html')

# api - test this api using postman
@app.route('/predict', methods = ['POST'])
def predict_api():
    data = request.json['data']
    new_data = np.array(list(data.values()))
    scaled_new_data = scaler.transform([new_data])
    output = model.predict(scaled_new_data)
    return jsonify(output[0])

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)
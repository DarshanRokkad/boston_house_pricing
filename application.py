from flask import Flask, request, url_for, jsonify, render_template
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
@app.route('/predict_api', methods = ['POST'])
def predict_api():
    data = request.json['data']
    new_data = np.array(list(data.values()))
    scaled_new_data = scaler.transform([new_data])
    output = model.predict(scaled_new_data)
    return jsonify(output[0])

# frontend application
@app.route('/predict', methods = ['POST'])
def prediction():
    # CRIM = float(request.form.get('CRIM'))
    new_data = [float(x) for x in request.form.values()]
    scaled_new_data = scaler.transform([new_data])
    output = model.predict(scaled_new_data)
    result_txt = f'Predicted House Price is {np.round(output[0], 2)}'
    return render_template('home.html', result = result_txt)
# Sample input :  0.00632	18.0	2.31	0.0	 0.538	6.575	65.2	4.0900	1.0	 296.0	15.3	396.90	4.98


if __name__ == '__main__':
    app.run(debug = True)
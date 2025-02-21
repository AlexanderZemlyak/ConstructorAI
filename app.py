import os
from flask import Flask, request, jsonify
from preprocessing import clean_text
from joblib import load

script_dir = os.path.dirname(__file__)

model_path = os.path.join(script_dir, 'logistic_regression_model.joblib')

model = load(model_path)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['x']
    
    prediction = model.predict_proba(data)
    
    prediction_list = prediction.tolist()
    
    return jsonify(prediction_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
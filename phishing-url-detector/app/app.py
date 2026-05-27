from flask import Flask, render_template, request
import pickle
import pandas as pd
import os

app = Flask(__name__)

# Load model and feature names
model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'phishing_model.pkl')
features_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'feature_names.pkl')

with open(model_path, 'rb') as f:
    model = pickle.load(f)

with open(features_path, 'rb') as f:
    feature_names = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html', features=feature_names)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = {}
        for feature in feature_names:
            value = request.form.get(feature, 0)
            input_data[feature] = int(value)

        input_df = pd.DataFrame([input_data])
        prediction = model.predict(input_df)[0]

        if prediction == -1:
            result = "PHISHING - This is a dangerous website!"
            color = "red"
        else:
            result = "LEGITIMATE - This website appears safe."
            color = "green"

    except Exception as e:
        result = f"Error: {str(e)}"
        color = "orange"

    return render_template('index.html', features=feature_names, result=result, color=color)

if __name__ == '__main__':
    app.run(debug=True)
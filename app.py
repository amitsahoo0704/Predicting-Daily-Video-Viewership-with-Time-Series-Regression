from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open('model/model.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)

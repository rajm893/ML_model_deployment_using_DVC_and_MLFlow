from flask import Flask, jsonify, request, render_template 
import os
import numpy as np
from prediction_service import prediction

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/predict_api", methods=["POST"])
def predict_api():
    print(request.json)
    response = prediction.predict(request.json)
    return jsonify(response)

@app.route('/predict' ,methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    response = prediction.predict_form(data)
    return render_template("home.html",prediction_text="The House price prediction is {}".format(response))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
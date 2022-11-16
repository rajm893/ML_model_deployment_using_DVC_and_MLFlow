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
    response = prediction.predict(request.json)
    return jsonify(response)

@app.route('/predict' ,methods=['POST'])
def predict():
    response = prediction.predict_form(request.form)
    return render_template("home.html",prediction_text="The House price \
                             prediction is {}".format(round(response,2)))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
import yaml
import os
import json
import joblib
import numpy as np


params_path = "params.yaml"

def read_params(config_path=params_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def predict(data):
    config = read_params(params_path)
    model_dir_path = config["webapp_model_dir"]
    model = joblib.load(model_dir_path)
    data = np.array(list(data.values())).reshape(1,-1)
    print(data)
    data = model.predict(data).tolist()[0]
    return data

def predict_form(data):
    config = read_params(params_path)
    model_dir_path = config["webapp_model_dir"]
    model = joblib.load(model_dir_path)
    data = np.array(data).reshape(1,-1)
    data = model.predict(data).tolist()[0]
    print(data)
    return data

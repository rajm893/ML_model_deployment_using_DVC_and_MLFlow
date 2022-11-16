import yaml
import os
import json
import joblib
import numpy as np


params_path = "params.yaml"
schema_path = os.path.join("prediction_service", "schema_in.json")


class NotInRange(Exception):
    def __init__(self, message="Values entered are not in expected range"):
        self.message = message
        super().__init__(self.message)


class NotInCols(Exception):
    def __init__(self, message="Not in cols"):
        self.message = message
        super().__init__(self.message)


def read_params(config_path=params_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def get_schema(schema_path=schema_path):
    with open(schema_path) as json_file:
        schema = json.load(json_file)
    return schema

def validate_input(dict_request):
    def _validate_cols(col):
        schema = get_schema()
        actual_cols = schema.keys()
        if col not in actual_cols:
            raise NotInCols

    def _validate_values(col, val):
        schema = get_schema()
        if not (schema[col]["min"] <= float(dict_request[col]) <= schema[col]["max"]) :
            raise NotInRange

    for col, val in dict_request.items():
        _validate_cols(col)
        _validate_values(col, val)
    return True

def predict(data):
    try:
        if validate_input(data):
            config = read_params(params_path)
            model_dir_path = config["webapp_model_dir"]
            model = joblib.load(model_dir_path)
            data = np.array(list(data.values())).reshape(1,-1)
            data = model.predict(data).tolist()[0]
            return data
    
    except NotInRange as e:
        response = {"the_exected_range": get_schema(), "response": str(e) }
        return response

    except NotInCols as e:
        response = {"the_exected_cols": get_schema().keys(), "response": str(e) }
        return response

    except Exception as e:
        response = {"response": str(e) }
        return response

def predict_form(data):

    if validate_input(data):
        config = read_params(params_path)
        model_dir_path = config["webapp_model_dir"]
        model = joblib.load(model_dir_path)
        data=[float(x) for x in data.values()]
        data = np.array(data).reshape(1,-1)
        data = model.predict(data).tolist()[0]
        return data


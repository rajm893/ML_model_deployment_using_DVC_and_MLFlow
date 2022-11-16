import os
import yaml
import pandas as pd
import argparse
from google.cloud import storage

def read_params(config_path):
    with open(config_path) as yml_file:
        config = yaml.safe_load(yml_file)
    return config

def get_data(config_path):
    config = read_params(config_path)
    gcp_source_path = config['data_source']['gcp_source']
    local_write_path = config['data_source']['local_write']
    project_name = config['gcp_details']["project_name"] 
    bucket_name = config['gcp_details']['bucket_name'] 
    storage_client = storage.Client(project_name)
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(gcp_source_path)
    blob.download_to_filename(local_write_path)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    data = get_data(config_path=parsed_args.config)
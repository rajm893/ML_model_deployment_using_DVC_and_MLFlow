## ML Model deployment using MLFLow and DVC




taxi_ml_model_893

5afb3b29-68bc-4471-a8b1-b58278d5f28e

artifact directotyr

mlflow server command

mlflow server \
        --backend-store-uri sqlite:///mlflow.db \
        --default-artifact-root ./artifacts \
        --host 0.0.0.0 -p 5555

pip install "dvc[gs]"
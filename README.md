## ML Model deployment using MLFLow and DVC


![ML Pipeline](/Misc/ML_pipeline.png "Workflow")




artifact directotyr

mlflow server command

mlflow server \
        --backend-store-uri sqlite:///mlflow.db \
        --default-artifact-root ./artifacts \
        --host 0.0.0.0 -p 5555

pip install "dvc[gs]"
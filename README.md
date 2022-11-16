# Automate ML Model deployment using DVC and MLFlow

![ML Pipeline](/Misc/ML_pipeline.png "Workflow")

* As the Continious Integration and Continious Deployment of Machine learning pipelines is important for Machine Learning Lifecycle, I  have demostrated the solution using [MLflow](https://mlflow.org/) and [DVC (Data Version Control)](https://dvc.org/).

* Here, the input data is tracked and maintained by DVC which uses git to track the .dvc files and Google cloud storage for storing data source. 

* The model pipeline like load, split, train and evaluate are executed in stages using dvc.yaml file. All the required configuration required during the ML pipeline is used from config file (params.yaml).<br>
Run below command to run the pipeline:
```
dvc repro
```
Run ```pytest -v``` to run all the test cases.
* Tracking of model stages like "logging of prediction model to production stage" is automated using MLflow. 

To use MLFlow UI run below command:
```
mlflow server \
        --backend-store-uri sqlite:///mlflow.db \
        --default-artifact-root ./artifacts \
        --host 0.0.0.0 -p 5555
```

* Here, the Application is served in two ways:<br>
    1. Prediction as a service using API
    1. Prediction using web UI 

* The prediction server is built using **Flask** and deployed the model on **Heroku** cloud.


* I have also used Github Actions for workflow using ci-cd.yaml (.github/workflows/ci-cd.yaml) for Continuous Integration and Continuous Deployment. The deployment is done once all the test cases are passed and the job is succeded.

Further Improvement: <br>

* Due to lack of resources couldn't leverage many functionalities Google cloud. We can run MLflow on the GCP VM instance and deploy the model using Google App Engine. 
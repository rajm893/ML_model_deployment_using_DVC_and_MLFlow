# Automated ML Deployment with DVC, MLFlow, and Cloud Integration


![ML Pipeline](/Misc/ML_pipeline.png "Workflow")

### 🎯 Project Aim
Simplify and automate the deployment of Machine Learning models using state-of-the-art CI/CD tools and cloud platforms.

### 🌟 Features

- 🔄 Continuous Integration & Deployment (CI/CD): Embrace the power of CI/CD for ML with [MLflow](https://mlflow.org/) and [DVC (Data Version Control)](https://dvc.org/).
- 📂 Data Management: Seamlessly track your input data with DVC, leveraging git for `.dvc` files and Google Cloud Storage for the actual data source.
- 🤖 Pipeline Automation: Execute the ML pipeline stages such as load, split, train, and evaluate via the `dvc.yaml` file. All configurations are managed using the `params.yaml`.

Run below command to run the pipeline:
  ```
  dvc repro
  ```
Run ```pytest -v``` to run all the test cases.

**Ensure your pipeline's robustness with**:

- 📊 Model Tracking: Effortlessly automate stages like "logging of prediction model to production" using MLflow.

To access the MLFlow UI:

``` 
mlflow server \
        --backend-store-uri sqlite:///mlflow.db \
        --default-artifact-root ./artifacts \
        --host 0.0.0.0 -p 5555
```


### Versatile Deployment:

- 🚀 API Service: Offer predictions on-the-go via a dedicated API.
- 🌐 Web UI: Enable users to make predictions through a web interface.
- ☁️ Cloud-Ready: Developed the prediction server using Flask and hosted it on the Heroku cloud platform.

- 🚀 Github Actions: Automate workflows using the `ci-cd.yaml` (located at `.github/workflows/ci-cd.yaml`). Deployment is triggered upon successful test case execution.

### 🔜 Future Directions

- Enhance cloud integration. Due to resource constraints, several Google Cloud functionalities were not tapped into. For instance:
  - Running MLflow on a GCP VM instance.
  - Model deployment via the Google App Engine to reduce latency given that artifacts and data would reside in Google Cloud Storage.
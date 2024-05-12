# MLOps Deployment Project 🚀

This project implements a modular object-oriented Pythonic approach to writing code, creating files like `config.yaml`, a utils file, and a configuration manager file to handle all configurations. Additionally, a components folder was created for strategies and two pipelines were implemented: training and prediction. The training pipeline includes data ingestion, base model creation, model training, and evaluation.

DVC orchestrates the pipeline, while MLflow manages model registry. Two images are included: one for all model experiments and one for model comparison. Docker is used for containerization. GitHub Actions and runners facilitate CI/CD, followed by deployment on AWS with EC2 and ECR.

## Modular Approach 🔧

The project follows a modular approach, organized into components and pipelines:

- **Config YAML File:** Contains configuration parameters for the project.
- **Components:** Individual modules or functions that perform specific tasks.
- **Pipelines:** Sequences of components orchestrated to execute machine learning workflows.

## Tools Used 🛠️

- **MLflow:** Used for model registry and management.
- **DVC (Data Version Control):** Utilized for pipeline orchestration and versioning data.
- **Dagshub:** Hosted repository for collaborative development and version control.
- **AWS Free Tier:** Utilized for cloud computing with a 1GB RAM instance.
- **Google Drive:** Used for storing project artifacts.
- **AWS EC2:** Hosting platform for deploying services and applications.
- **AWS ECR (Elastic Container Registry):** Used for storing and managing Docker container images.
- **Docker:** Containerization technology for packaging applications and dependencies.
- **Streamlit:** Web application framework used for interactive data visualization.

## CI/CD with GitHub Actions 🚀

Continuous Integration and Continuous Deployment (CI/CD) pipelines are implemented using GitHub Actions. The pipelines automate the build, test, and deployment processes, delivering the project to AWS services.

[Check out CI/CD workflows](https://github.com/harshpatel1242/MLOps_Deployment/actions)

## Pipeline Flow 📊

![Pipeline Flow](https://github.com/harshpatel1242/MLOps_Deployment/blob/master/Pipeline_Flow.PNG)

## Project Repository 📁

The complete project code and resources can be accessed on Dagshub:

[Link to Dagshub Repository](https://dagshub.com/harshpatel1242/MLOps_Deployment)

## MLflow Experiments & Comaprisions 📁
![MLFlow_Exp](https://github.com/harshpatel1242/MLOps_Deployment/blob/master/MLFlow_Exp.PNG)
![Model_Comparision](https://github.com/harshpatel1242/MLOps_Deployment/blob/master/Model_Comparision.PNG)

## AWS Services ☁️

The project utilizes AWS Free Tier services for cloud computing, including EC2 for hosting and ECR for Docker image management. Make sure to manage resources within the Free Tier limits.

## Artifact Storage 📂

All project artifacts, including data, models, and logs, are stored on Google Drive.

## Data Access 📊

The project's data can be accessed from Google Drive using the following link:

[Google Drive Data Link](https://drive.google.com/file/d/1Q02T8c6-BRC32TbSFqZdLpR9UdVeVpHS/view?usp=drive_link)

Feel free to explore the project repository for more details and contributions.

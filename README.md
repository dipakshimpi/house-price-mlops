🏠 House Price Prediction MLOps Project

This project demonstrates a complete MLOps workflow using a Machine Learning model to predict house prices based on basic features like number of bedrooms, bathrooms, and area.

It includes:

✔️ Model training
✔️ FastAPI-based web API
✔️ Docker containerization
✔️ Automated CI/CD pipeline with GitHub Actions
✔️ Docker image publishing to DockerHub

🔥 Project Architecture
house-price-mlops/
│
├── app/                 # FastAPI application
│   ├── main.py
│   ├── utils.py
│   └── requirements.txt
│
├── model/               # Model training script
│   └── train_model.py
│
├── data/                # Training dataset
│   └── house_price.csv
│
├── Dockerfile           # Docker build instructions
├── .github/workflows    # GitHub Actions CI/CD pipeline
│   └── ci-cd.yml
└── README.md            # Project documentation

🚀 Features

🧠 Trained ML model using scikit-learn

⚡ REST API built with FastAPI

🐳 Fully Dockerized application

🔁 CI/CD using GitHub Actions

📦 Automatic Docker image push to DockerHub

🛠️ Tech Stack
Layer	Technology
Model	Python, scikit-learn
API	FastAPI
Packaging	Docker
CI/CD	GitHub Actions
Registry	DockerHub
📦 Docker Setup
🏗️ Build Docker Image
docker build -t dipak45/house-price-api .

▶️ Run Container
docker run -p 8000:8000 dipak45/house-price-api

🌐 API Usage

Once the container is running, open:

http://localhost:8000

🔮 Predict Example

POST request:

http://localhost:8000/predict?bedrooms=3&bathrooms=2&area=1200


Response:

{
  "predicted_price": 245000.0
}

🔁 CI/CD Pipeline

Every push to the main branch triggers:

Checkout repository

Build Docker image

Login to DockerHub (secrets-based auth)

Push image to DockerHub

🐳 DockerHub Image

You can pull the latest image from:

https://hub.docker.com/r/dipak45/house-price-api

📂 GitHub Repository
https://github.com/dipakshimpi/house-price-mlops

🚧 Future Enhancements

🌍 Cloud deployment (Render / AWS / GCP)

🎯 Monitoring and logging

🧪 Unit tests integration

📈 Model retraining pipeline

🙌 Author

Dipak Shimpi
MLOps & ML Enthusiast

⭐ Contributing

Pull requests are welcome!
Feel free to fork the repo and explore improvements.






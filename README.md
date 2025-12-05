🏠 House Price Prediction — End-to-End MLOps Project

This project demonstrates a complete MLOps workflow to predict house prices using a Machine Learning model trained on features like bedrooms, bathrooms, and area.

It includes:

✔️ Model Training
✔️ FastAPI Web API
✔️ Docker Containerization
✔️ CI/CD Pipeline with GitHub Actions
✔️ Docker Image Publishing to DockerHub

📁 Project Structure
house-price-mlops/
├── app/                     # FastAPI application
│   ├── main.py
│   ├── utils.py
│   └── requirements.txt
├── frontend/                # Streamlit UI (optional)
│   └── app.py
├── model/                   # Model training script
│   └── train_model.py
├── data/                    # Training dataset
│   └── house_price.csv
├── Dockerfile               # Docker build file for backend
├── docker-compose.yml       # Multi-container setup (frontend + backend)
├── .github/workflows        # CI/CD pipeline
│   └── ci-cd.yml
└── README.md

🚀 Features
Feature	Description
🧠 Model	Trained using scikit-learn
⚡ API	Built using FastAPI
🐳 Containers	Fully Dockerized
🔁 CI/CD	Implemented using GitHub Actions
📦 Registry	Auto-push image to DockerHub
🐍 Train the Model
python model/train_model.py


This generates model.pkl which is used by FastAPI for predictions.

⚡ Run API Locally
1️⃣ Install dependencies
pip install -r app/requirements.txt

2️⃣ Start FastAPI server
uvicorn app.main:app --reload


Open API docs:

👉 http://localhost:8000/docs

🐳 Docker Setup
🏗️ Build Docker Image
docker build -t dipak45/house-price-api .

▶️ Run Container
docker run -p 8000:8000 dipak45/house-price-api

🌐 API Usage
🔮 Predict Example

POST request:

http://localhost:8000/predict?bedrooms=3&bathrooms=2&area=1200

Response:
{
  "predicted_price": 245000.0
}

🔁 CI/CD Pipeline (GitHub Actions)

Every push to the main branch triggers:

✔️ Checkout repository
✔️ Build Docker image
✔️ Login to DockerHub (using secrets)
✔️ Push image to DockerHub


CI/CD file: .github/workflows/ci-cd.yml

🐳 DockerHub Image

Pull latest image:

docker pull dipak45/house-price-api


DockerHub URL👇
🔗 https://hub.docker.com/r/dipak45/house-price-api

📂 GitHub Repository

🔗 https://github.com/dipakshimpi/house-price-mlops

🚧 Future Enhancements
Feature	Status
🌍 Cloud deployment (Render/AWS/GCP)	🔜
🎯 Monitoring & Logging	🔜
🧪 Unit Tests	🔜
♻️ Model Retraining Pipeline	🔜
🙌 Author

👤 Dipak Shimpi
ML & MLOps Enthusiast 🚀

⭐ Contributing

Pull requests are welcome! Feel free to fork, explore, and improve this project.
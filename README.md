.

🏡 House Price Prediction — End-to-End MLOps Project

This project demonstrates a complete MLOps workflow for predicting house prices using a Machine Learning model trained on features like bedrooms, bathrooms, and area. The system is automated using FastAPI, Docker, and GitHub Actions, with the trained model served through a production-ready API.

🚀 Highlights
Feature	Description

🧠 ML Model	Trained using scikit-learn
⚡ API	Developed with FastAPI
🐳 Dockerized	Fully containerized backend
🔁 CI/CD	Automated pipeline via GitHub Actions
📦 Registry	Docker images pushed to DockerHub


📁 Project Structure
house-price-mlops/
├── app/                       # FastAPI backend service
│   ├── main.py                # API endpoints
│   ├── utils.py               # Helper utilities
│   └── requirements.txt       # Backend dependencies
│
├── frontend/                  # Streamlit UI (optional)
│   └── app.py
│
├── model/                     # ML model training workflow
│   └── train_model.py
│
├── data/                      # Training dataset
│   └── house_price.csv
│
├── Dockerfile                 # Docker build config for backend
├── docker-compose.yml         # Multi-container setup (UI + API)
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # CI/CD automation pipeline
│
└── README.md                  # Project documentation

🧠 Model Training

Run the model training script:

python model/train_model.py


This generates model.pkl, which is automatically loaded by FastAPI during runtime.

⚡ Run API Locally
Install dependencies
pip install -r app/requirements.txt

Start FastAPI server
uvicorn app.main:app --reload


Swagger UI will be available at:

👉 http://localhost:8000/docs

🐳 Docker Setup
Build Docker Image
docker build -t dipak45/house-price-api .

Run Docker Container
docker run -p 8000:8000 dipak45/house-price-api


Access the API at:

👉 http://localhost:8000

🌐 API Usage
Prediction Request
POST http://localhost:8000/predict?bedrooms=3&bathrooms=2&area=1200

Example Response
{
  "predicted_price": 245000.0
}

🔁 CI/CD Pipeline (GitHub Actions)

The CI/CD workflow performs:

✔️ Checkout repository
✔️ Build Docker image
✔️ Authenticate to DockerHub
✔️ Push image to registry


Pipeline file:

.github/workflows/ci-cd.yml

🐳 DockerHub Image

Pull the latest image:

docker pull dipak45/house-price-api


🔗 https://hub.docker.com/r/dipak45/house-price-api

📦 GitHub Repository

🔗 https://github.com/dipakshimpi/house-price-mlops

🚧 Future Enhancements

🌍 Deploy to cloud platforms (AWS / GCP / Render)

📊 Add monitoring and logging stack

🧪 Integrate unit and API tests

🔁 Automated retraining pipeline

👤 Author

Dipak Shimpi
MLOps & Machine Learning Enthusiast

⭐ Contributing

Contributions are welcome!
Fork the repo, explore improvements, and submit a pull request 🚀
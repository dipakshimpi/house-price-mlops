🏡 House Price Prediction — MLOps Pipeline Project

This project showcases a practical MLOps workflow to predict house prices using a Machine Learning model. The system is fully automated using FastAPI, Docker, and GitHub Actions, enabling continuous integration and delivery.


🚀 What This Project Offers

| Capability          | Description                             |
| ------------------- | --------------------------------------- |
| 🧠 ML Model         | Trained using **scikit-learn**          |
| ⚡ REST API          | Served using **FastAPI**                |
| 🐳 Containerization | Complete deployment with **Docker**     |
| 🔁 CI/CD Pipeline   | Automated builds via **GitHub Actions** |
| 📦 Image Registry   | Docker image pushed to **DockerHub**    |

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
├── Dockerfile                 # Docker build configuration for backend
├── docker-compose.yml         # Multi-container setup (API + UI)
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # Automated CI/CD pipeline
│
└── README.md                  # Project documentation

🧠 Model Training

A regression model is trained using train_model.py, and the trained model is stored as model.pkl.

python model/train_model.py

The FastAPI backend loads this model at runtime for serving predictions.


⚡ Run the API Locally
1️⃣ Install Required Packages
pip install -r app/requirements.txt

2️⃣ Launch API Server
uvicorn app.main:app --reload


📌 Interactive API docs available at:
👉 http://localhost:8000/docs


🐳 Docker Deployment
🔨 Build Docker Image
docker build -t dipak45/house-price-api .

▶️ Run the Container
docker run -p 8000:8000 dipak45/house-price-api


Once running, the API is accessible at:

👉 http://localhost:8000


🌐 Predict Using API
🔮 Make a Prediction Request
http://localhost:8000/predict?bedrooms=3&bathrooms=2&area=1200


Sample Response

{
  "predicted_price": 245000.0
}

🔁 CI/CD Pipeline

Every push to the main branch triggers automation:

✔️ Checkout source code
✔️ Build Docker Image
✔️ Authenticate to DockerHub
✔️ Push image to registry


CI/CD file: .github/workflows/ci-cd.yml

🐳 DockerHub Image

Pull the latest build:

docker pull dipak45/house-price-api


🔗 https://hub.docker.com/r/dipak45/house-price-api

📁 Repository Link

🔗 https://github.com/dipakshimpi/house-price-mlops

🚧 Roadmap / Next Steps

🌍 Deploy API to cloud (AWS / GCP / Render)

📊 Add monitoring (Prometheus / Grafana)

🧪 Integrate automated testing

🔁 Enable continuous model retraining

🙋 Author

Dipak Shimpi
MLOps & Machine Learning Explorer

🌟 Want to Contribute?

Feel free to fork the project, create enhancements, and submit PRs. Contributions are always welcome!
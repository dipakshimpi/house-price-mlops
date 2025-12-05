# 🏠 House Price Prediction — End-to-End MLOps Project

This project demonstrates a complete MLOps workflow for predicting house prices using a machine learning model based on features such as **bedrooms**, **bathrooms**, and **area**.

---

| Feature                 |                Description                                          |
| ----------------------- | ------------------------------------------------------------------------------ |
| 🧠 ML Model Training    | Built using **scikit-learn**, trained on real estate dataset                   |
| ⚡ FastAPI Backend       | High-performance REST API for serving real-time predictions                  
|
| 🐳 Full Dockerization   | Backend & dependencies containerized for portable and consistent deployment    |
| 🔁 GitHub Actions CI/CD | Automated pipeline builds Docker image on each push and pushes to DockerHub    |
| 📦 DockerHub Registry   | Stores production-ready images for deployment across any environment           |
| 🧱 Modular Architecture | Clean separation of **model**, **API**, and **UI** for scalable development    |
| 🚀 Ready for Cloud      | Architecture compatible with AWS, GCP, Azure, and Kubernetes-based deployments |

---

## 📂 Project Structure

```bash
house-price-mlops/
├── app/                     # FastAPI backend
│   ├── main.py
│   ├── utils.py
│   └── requirements.txt
├── frontend/                # Streamlit UI (optional)
│   └── app.py
├── model/                   # Model training script
│   └── train_model.py
├── data/                    # Training dataset
│   └── house_price.csv
├── Dockerfile               # Build file for backend
├── docker-compose.yml       # Multicontainer setup (frontend + backend)
├── .github/workflows
│   └── ci-cd.yml            # CI/CD pipeline
└── README.md
🧠 Model Training
The model is trained using train_model.py and saved as model.pkl.

bash
Copy code
python model/train_model.py
This model is loaded by FastAPI during runtime to serve predictions.

⚡ Run API Locally
1️⃣ Install Dependencies
bash
Copy code
pip install -r app/requirements.txt
2️⃣ Start FastAPI Server
bash
Copy code
uvicorn app.main:app --reload
Open API documentation:

👉 http://localhost:8000/docs

🐳 Docker Setup
🏗️ Build Docker Image
bash
Copy code
docker build -t dipak45/house-price-api .
▶️ Run Container
bash
Copy code
docker run -p 8000:8000 dipak45/house-price-api
🌐 API Usage
🔮 Prediction Request
bash
Copy code
POST http://localhost:8000/predict?bedrooms=3&bathrooms=2&area=1200
Example Response
json
Copy code
{
  "predicted_price": 245000.0
}
🔁 CI/CD Pipeline
Every push to the main branch triggers:

Clone repository

Build Docker image

Authenticate with DockerHub (via GitHub Secrets)

Push updated image to DockerHub

Pipeline file:
.github/workflows/ci-cd.yml

🐳 DockerHub Image
Pull the latest backend image:

bash
Copy code
docker pull dipak45/house-price-api
🔗 https://hub.docker.com/r/dipak45/house-price-api

📦 GitHub Repository
🔗 https://github.com/dipakshimpi/house-price-mlops

🚀 Future Enhancements
🌍 Cloud deployment (AWS / GCP / Render)

🎯 Monitoring & logging

🧪 Unit test integration

🔁 Automated model retraining pipeline

🙌 Author
Dipak Shimpi
MLOps & ML Enthusiast

⭐ Contributing
Pull requests are welcome! Feel free to fork this repository and explore improvements
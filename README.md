  <div align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/6122/6122753.png" width="100" height="100" alt="MLOps Logo">
  <h1>🏡 House Price Prediction</h1>
  <p><b>End-to-End MLOps Project</b></p>

  <p>
    <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI">
    <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
    <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white" alt="CI/CD">
    <img src="https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="sklearn">
  </p>
</div>

---

### 📝 Overview
This project demonstrates a complete **MLOps workflow** for predicting house prices. It covers the entire lifecycle from model training to containerized deployment and automated CI/CD pipelines.



---

### 🚀 Highlights
<table width="100%">
  <tr>
    <th width="30%">Feature</th>
    <th width="70%">Description</th>
  </tr>
  <tr>
    <td><b>🧠 ML Model</b></td>
    <td>Linear Regression trained using <code>scikit-learn</code>.</td>
  </tr>
  <tr>
    <td><b>⚡ API</b></td>
    <td>High-performance backend developed with <code>FastAPI</code>.</td>
  </tr>
  <tr>
    <td><b>🐳 Dockerized</b></td>
    <td>Fully containerized environment for seamless deployment.</td>
  </tr>
  <tr>
    <td><b>🔁 CI/CD</b></td>
    <td>Automated Build-Test-Push pipeline via <code>GitHub Actions</code>.</td>
  </tr>
  <tr>
    <td><b>📦 Registry</b></td>
    <td>Automated image versioning pushed to <code>DockerHub</code>.</td>
  </tr>
</table>

---

### 📁 Project Structure
<details>
<summary><b>▶ Click to expand structure</b></summary>

```text
house-price-mlops/
├── app/                        # FastAPI backend service
│   ├── main.py                 # API endpoints
│   ├── utils.py                # Helper utilities
│   └── requirements.txt        # Backend dependencies
├── frontend/                   # Streamlit UI (optional)
│   └── app.py
├── model/                      # ML model training workflow
│   └── train_model.py
├── data/                       # Training dataset
│   └── house_price.csv
├── Dockerfile                  # Docker build config
├── docker-compose.yml          # Multi-container setup
├── .github/
│   └── workflows/
│       └── ci-cd.yml           # CI/CD automation pipeline
└── README.md                   # Project documentation




🧠 Model Training
To retrain the model and update the model.pkl file, execute the training script:

Bash

python model/train_model.py
⚡ Local Execution
Install Dependencies:

Bash

pip install -r app/requirements.txt
Start FastAPI Server:

Bash

uvicorn app.main:app --reload
Explore Swagger UI: Access the interactive API documentation at: http://localhost:8000/docs

🐳 Docker Workflow
You can build and run the application inside a container to ensure environment consistency.

Build the image:

Bash

docker build -t dipak45/house-price-api .
Run the container:

Bash

docker run -p 8000:8000 dipak45/house-price-api
🌐 API Usage
Request: POST http://localhost:8000/predict?bedrooms=3&bathrooms=2&area=1200

Response:

JSON

{
  "predicted_price": 245000.0
}
🔁 CI/CD Pipeline
The GitHub Actions workflow automates the following steps on every push to the main branch:

✔️ Checkout Repository: Pulls the latest code.

✔️ Build Docker Image: Packages the application.

✔️ Authenticate to DockerHub: Securely logs into the registry.

✔️ Push Image to Registry: Updates the image on DockerHub.

🚧 Future Enhancements
[ ] 🌍 Cloud Deployment: Migrate to AWS (EC2/ECS) or GCP.

[ ] 📊 Monitoring: Integrate Prometheus and Grafana for model drift tracking.

[ ] 🧪 Testing: Add PyTest for unit and integration testing.

[ ] 🔁 Retraining: Implement automated retraining triggers.

👤 Author
Dipak Shimpi MLOps & Machine Learning Enthusiast

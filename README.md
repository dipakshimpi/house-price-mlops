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
To retrain the model and update the model.pkl file, execute:

Bash

python model/train_model.py
⚡ Local Execution
<ol> <li><b>Install Dependencies:</b> <pre><code>pip install -r app/requirements.txt</code></pre> </li> <li><b>Start FastAPI Server:</b> <pre><code>uvicorn app.main:app --reload</code></pre> </li> <li><b>Explore Swagger UI:</b> <br />👉 <a href="http://localhost:8000/docs">http://localhost:8000/docs</a> </li> </ol>

🐳 Docker Workflow
Build and run the container locally:

Bash

# Build
docker build -t dipak45/house-price-api .

# Run
docker run -p 8000:8000 dipak45/house-price-api
🌐 API Usage
<b>Request:</b> POST http://localhost:8000/predict?bedrooms=3&bathrooms=2&area=1200

<b>Response:</b>

JSON

{
  "predicted_price": 245000.0
}
🔁 CI/CD Pipeline
The GitHub Actions workflow automates the following steps on every push to the main branch:

<ul> <li>✔️ Checkout Repository</li> <li>✔️ Build Docker Image</li> <li>✔️ Authenticate to DockerHub</li> <li>✔️ Push Image to Registry</li> </ul>

🚧 Future Enhancements
[ ] 🌍 Cloud Deployment: Migrate to AWS (EC2/ECS) or GCP.

[ ] 📊 Monitoring: Integrate Prometheus and Grafana for model drift.

[ ] 🧪 Testing: Add PyTest for unit and integration testing.

[ ] 🔁 Retraining: Implement automated retraining triggers.

👤 Author
<p> <b>Dipak Shimpi</b><br /> <i>MLOps & Machine Learning Enthusiast</i> </p>

<p> <a href="https://github.com/dipakshimpi/house-price-mlops"> <img src="https://www.google.com/search?q=https://img.shields.io/badge/GitHub-100000%3Fstyle%3Dfor-the-badge%26logo%3Dgithub%26logoColor%3Dwhite" alt="GitHub"> </a> <a href="https://hub.docker.com/r/dipak45/house-price-api"> <img src="https://www.google.com/search?q=https://img.shields.io/badge/DockerHub-2496ED%3Fstyle%3Dfor-the-badge%26logo%3Ddocker%26logoColor%3Dwhite" alt="DockerHub"> </a> </p>

<div align="center"> <sub>⭐ If you find this project useful, please consider giving it a star!</sub> </div>

from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def home():
    return {"message": "House Price Prediction API is running!"}

@app.post("/predict")
def predict_price(bedrooms: int, bathrooms: int, area: int):
    data = np.array([[bedrooms, bathrooms, area]])
    price = model.predict(data)[0]
    return {"predicted_price": price}

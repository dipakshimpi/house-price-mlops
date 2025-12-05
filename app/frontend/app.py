import streamlit as st
import requests
import os

st.title("🏠 House Price Prediction App")

bedrooms = st.number_input("Bedrooms", min_value=1, step=1)
bathrooms = st.number_input("Bathrooms", min_value=1, step=1)
area = st.number_input("Area (sqft)", min_value=300, step=100)

if st.button("Predict Price"):

    backend_url = os.getenv("BACKEND_URL", "http://localhost:8000")

    response = requests.post(
        f"{backend_url}/predict",
        params={
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "area": area
        }
    )

    prediction = response.json()["predicted_price"]
    st.success(f"Predicted House Price: ₹ {prediction:,.2f}")

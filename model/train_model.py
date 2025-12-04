import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv("house_price.csv")

X = data[["bedrooms", "bathrooms", "area"]]
y = data["price"]

model = LinearRegression()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved inside container!")

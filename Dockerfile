FROM python:3.10

WORKDIR /app

# Copy app code
COPY app/ /app/

# Copy training script and data
COPY model/train_model.py /app/train_model.py
COPY data/house_price.csv /app/house_price.csv

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Train the model inside the container
RUN python train_model.py

# Expose port
EXPOSE 8000

# Start FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

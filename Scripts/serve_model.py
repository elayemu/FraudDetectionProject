### Task 4: Model Deployment and API Development
#### Setting Up the Flask API

from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Placeholder for model prediction logic
    return jsonify({'prediction': 'fraud' if data['amount'] > 1000 else 'not fraud'})

if __name__ == '__main__':
    app.run(debug=True)

#### Dockerizing the Flask Application
# Create a Dockerfile:

FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "serve_model.py"]

# Build and Run Docker

docker build -t fraud-detection-model .
docker run -p 5000:5000 fraud-detection-model
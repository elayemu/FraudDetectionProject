# Fraud Detection Project

## Description
This project aims to improve fraud detection for e-commerce and banking transactions using machine learning models. It involves data preprocessing, feature engineering, and model training to enhance fraud detection accuracy. The datasets used include:

- **Fraud_Data.csv**: Contains e-commerce transaction data with fraud labels.
- **IpAddress_to_Country.csv**: Maps IP addresses to country locations.
- **creditcard.csv**: Contains bank transaction data with fraud labels.

## Project Structure
FraudDetectionProject/ │-- data/ # Contains raw datasets │-- notebooks/ # Jupyter notebooks for analysis │-- scripts/ # Python scripts for preprocessing & modeling │-- models/ # Saved models │-- README.md # Project documentation │-- requirements.txt # Dependencies │-- .gitignore # Ignore unnecessary files

## Installation & Setup
1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd FraudDetectionProject
## Create and activate a virtual environment:
python -m venv venv
venv\Scripts\activate  
## Install dependencies
pip install -r requirements.txt
## Data Preprocessing Steps
Handling missing values
Removing duplicates
Correcting data types
Exploratory Data Analysis (EDA)
Merging datasets for geolocation analysis
Feature engineering (transaction frequency, time-based features)
Normalization and categorical encoding
## Running the Preprocessing Script
To execute the data preprocessing steps, run:
python scripts/preprocess_data.py
## License
This project is licensed under the MIT License.


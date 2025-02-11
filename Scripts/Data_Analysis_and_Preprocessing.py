import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ipaddress
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Load data
fraud_data = pd.read_csv(r'C:\Users\b102western\FraudDetectionProject\data\Fraud_Data.csv')
ip_data = pd.read_csv(r'C:\Users\b102western\FraudDetectionProject\data\IpAddress_to_Country.csv')
credit_data = pd.read_csv(r'C:\Users\b102western\FraudDetectionProject\data\creditcard.csv')

# Clean data
fraud_data = fraud_data.dropna()
ip_data = ip_data.dropna()
credit_data = credit_data.dropna()

fraud_data['signup_time'] = pd.to_datetime(fraud_data['signup_time'])
fraud_data['purchase_time'] = pd.to_datetime(fraud_data['purchase_time'])

# Plots for Data Visualization
sns.histplot(fraud_data['purchase_value'], bins=30, kde=True)
plt.title('Distribution of Purchase Value')
plt.savefig('distribution_of_purchase_value.png')  # Save plot as PNG
plt.close()  # Close the plot

sns.boxplot(x='class', y='purchase_value', data=fraud_data)
plt.title('Purchase Value Distribution by Fraud Class')
plt.savefig('purchase_value_distribution_by_fraud_class.png')  # Save plot as PNG
plt.close()  # Close the plot

# Function to convert IP address to integer, with validation
def ip_to_int(ip):
    try:
        return int(ipaddress.IPv4Address(ip))
    except ipaddress.AddressValueError:  # Handle invalid IP addresses
        return None  # or you can choose to return a specific integer (e.g., 0)

# Apply function to fraud_data, but first filter valid IP addresses
fraud_data['ip_address'] = fraud_data['ip_address'].apply(ip_to_int)

# Optionally, drop rows where ip_address could not be converted
fraud_data = fraud_data.dropna(subset=['ip_address'])

# Merge data
merged_data = fraud_data.merge(ip_data, left_on='ip_address', right_on='lower_bound_ip_address', how='left')

# Additional analytics
fraud_data['transaction_count'] = fraud_data.groupby('user_id')['user_id'].transform('count')
fraud_data['hour_of_day'] = fraud_data['purchase_time'].dt.hour
fraud_data['day_of_week'] = fraud_data['purchase_time'].dt.weekday

# Scale data
scaler = MinMaxScaler()
fraud_data['purchase_value'] = scaler.fit_transform(fraud_data[['purchase_value']])

# Encode categorical features
encoder = LabelEncoder()
fraud_data['source'] = encoder.fit_transform(fraud_data['source'])
fraud_data['browser'] = encoder.fit_transform(fraud_data['browser'])
fraud_data['sex'] = encoder.fit_transform(fraud_data['sex'])
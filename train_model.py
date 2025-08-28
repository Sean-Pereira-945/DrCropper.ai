import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# Load the dataset first to check column names
data = pd.read_csv('Crop_recommendation.csv')
print("Available columns in dataset:", data.columns.tolist())

# Define features (adjusted to match actual column names)
features = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']  # Changed 'pH' to 'ph'

# Validate that all required features are present
missing_features = set(features) - set(data.columns)
if missing_features:
    raise ValueError(f"Missing required features: {missing_features}")

X = data[features]  # All 7 features
y = data['label']

# Validate feature dimensions
if X.shape[1] != 7:
    raise ValueError(f"Model expects 7 features, but got {X.shape[1]}")

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train, y_train)

# Calculate and print accuracy
train_accuracy = model.score(X_train, y_train)
test_accuracy = model.score(X_test, y_test)
print(f"Training Accuracy: {train_accuracy:.2f}")
print(f"Testing Accuracy: {test_accuracy:.2f}")
print(f"Feature names used: {features}")

# Save the model and feature names
model_data = {
    'model': model,
    'features': features
}
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
with open(model_path, "wb") as f:
    pickle.dump(model_data, f)

print(f"Model trained and saved to: {model_path}")
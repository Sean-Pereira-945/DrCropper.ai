import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import os

# Create flask app
flask_app = Flask(__name__)

# Define all required features - updated 'pH' to 'ph' to match training data
REQUIRED_FEATURES = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']

# Get the absolute path to the model file
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

# Load the model with error handling
try:
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Model file not found: {MODEL_PATH}\n"
            "Please ensure you have trained the model and saved it as 'model.pkl'"
        )
    with open(MODEL_PATH, "rb") as f:
        model_data = pickle.load(f)
        model = model_data['model']
        features = model_data['features']
    
    # Validate that model expects all required features
    if set(features) != set(REQUIRED_FEATURES):
        raise ValueError(f"Model expects features {REQUIRED_FEATURES}, but got {features}")

except Exception as e:
    print(f"Error loading model: {e}")
    raise

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods=["POST"])
def predict():
    try:
        # Debug: Print all form data
        print("Form data received:", request.form)
        print("Form keys:", list(request.form.keys()))
        
        # Get all 7 features from the form
        feature_values = []
        for feature in REQUIRED_FEATURES:
            value = request.form.get(feature)
            print(f"Getting feature {feature}: {value}")  # Debug print
            if value is None or value.strip() == '':
                raise ValueError(f"Missing required feature: {feature}")
            feature_values.append(float(value))
        
        # Print received values for debugging
        print(f"Received features: {dict(zip(REQUIRED_FEATURES, feature_values))}")
        
        # Reshape for sklearn (1 sample, 7 features)
        features_array = np.array(feature_values).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(features_array)
        
        return render_template(
            "index.html", 
            prediction_text=f"The Recommended Crop is: {prediction[0]}"
        )
    except ValueError as e:
        return render_template(
            "index.html", 
            prediction_text=f"Invalid input: {str(e)}"
        )
    except Exception as e:
        return render_template(
            "index.html", 
            prediction_text=f"Error making prediction: {str(e)}"
        )

if __name__ == "__main__":
    flask_app.run(debug=True)
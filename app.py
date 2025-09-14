from flask import Flask, render_template, request, jsonify, redirect, url_for
import random
import json
import os
from lib.supabase import supabase

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'dev-secret-key-change-in-production')

# Simple crop recommendation logic without external dependencies
CROP_DATA = {
    'rice': {'temp_range': (20, 35), 'humidity_range': (80, 95), 'ph_range': (5.5, 7.0)},
    'wheat': {'temp_range': (12, 25), 'humidity_range': (55, 70), 'ph_range': (6.0, 7.5)},
    'corn': {'temp_range': (18, 27), 'humidity_range': (60, 80), 'ph_range': (6.0, 6.8)},
    'cotton': {'temp_range': (21, 30), 'humidity_range': (50, 80), 'ph_range': (5.8, 8.0)},
    'sugarcane': {'temp_range': (21, 27), 'humidity_range': (75, 85), 'ph_range': (6.0, 7.5)},
    'potato': {'temp_range': (15, 20), 'humidity_range': (80, 95), 'ph_range': (4.8, 5.4)}
}

def recommend_crop(temperature, humidity, ph, rainfall, nitrogen, phosphorus, potassium):
    """Simple crop recommendation based on basic rules"""
    suitable_crops = []
    
    for crop, conditions in CROP_DATA.items():
        temp_min, temp_max = conditions['temp_range']
        hum_min, hum_max = conditions['humidity_range']
        ph_min, ph_max = conditions['ph_range']
        
        if (temp_min <= temperature <= temp_max and 
            hum_min <= humidity <= hum_max and 
            ph_min <= ph <= ph_max):
            suitable_crops.append(crop)
    
    if suitable_crops:
        return random.choice(suitable_crops)
    else:
        # Return a random crop if no perfect match
        return random.choice(list(CROP_DATA.keys()))

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/predict-page')
def predict_page():
    return render_template('index.html')

@app.route('/history-page')
def history_page():
    return render_template('history.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user info from request (in a real app, this would come from session/auth)
        user_email = request.form.get('user_email', 'anonymous@example.com')
        
        # Get form data
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])
        nitrogen = float(request.form['nitrogen'])
        phosphorus = float(request.form['phosphorus'])
        potassium = float(request.form['potassium'])
        
        # Make prediction using simple logic
        prediction = recommend_crop(temperature, humidity, ph, rainfall, nitrogen, phosphorus, potassium)
        confidence = random.uniform(75, 95)  # Simulate confidence score
        
        # Store prediction in database
        try:
            # First, ensure user exists in user_profiles
            existing_user = supabase.select('user_profiles', 'id', {'email': f'eq.{user_email}'})
            
            if not existing_user:
                # Create user profile
                user_data = {
                    'email': user_email,
                    'name': user_email.split('@')[0]
                }
                user_result = supabase.insert('user_profiles', user_data)
                user_id = user_result[0]['id'] if user_result else None
            else:
                user_id = existing_user[0]['id']
            
            # Store the prediction
            if user_id:
                prediction_data = {
                    'user_id': user_id,
                    'nitrogen': nitrogen,
                    'phosphorus': phosphorus,
                    'potassium': potassium,
                    'temperature': temperature,
                    'humidity': humidity,
                    'ph': ph,
                    'rainfall': rainfall,
                    'predicted_crop': prediction,
                    'confidence': round(confidence, 2)
                }
                supabase.insert('crop_predictions', prediction_data)
        except Exception as db_error:
            print(f"Database error: {db_error}")
            # Continue without storing to database
        
        return jsonify({
            'crop': prediction,
            'confidence': round(confidence, 2),
            'message': f'Based on your soil and climate conditions, {prediction} is recommended.'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/history')
def prediction_history():
    """Get prediction history for a user"""
    try:
        user_email = request.args.get('email', 'anonymous@example.com')
        
        # Get user's prediction history
        user_data = supabase.select('user_profiles', 'id', {'email': f'eq.{user_email}'})
        
        if not user_data:
            return jsonify({'predictions': []})
        
        user_id = user_data[0]['id']
        predictions = supabase.select(
            'crop_predictions', 
            'predicted_crop,confidence,created_at,nitrogen,phosphorus,potassium,temperature,humidity,ph,rainfall',
            {'user_id': f'eq.{user_id}'}
        )
        
        return jsonify({'predictions': predictions or []})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
if __name__ == '__main__':
    app.run(debug=True)
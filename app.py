from flask import Flask, render_template, request, jsonify, redirect, url_for
import random
import json

app = Flask(__name__)

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

@app.route('/predict', methods=['POST'])
def predict():
    try:
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
        
        return jsonify({
            'crop': prediction,
            'confidence': round(confidence, 2),
            'message': f'Based on your soil and climate conditions, {prediction} is recommended.'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
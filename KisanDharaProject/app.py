from flask import Flask, render_template, request, jsonify
from models import predict_crop

# Initialize Flask app
app = Flask(__name__)

# Route for start page (landing page)
@app.route('/')
def start():
    return render_template('start.html')

# Route for authentication page
@app.route('/auth')
def auth():
    return render_template('auth.html')

# Route for home page
@app.route('/home')
def home():
    return render_template('home.html')

# Route for AI assistant page
@app.route('/ai-assistant')
def ai_assistant():
    return render_template('ai-assistant.html')

# Route for weather page
@app.route('/weather')
def weather():
    return render_template('weather.html')

# Route for market page
@app.route('/market')
def market():
    return render_template('market.html')

# API endpoint for crop prediction
@app.route('/predict_crop', methods=['POST'])
def predict_crop_api():
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Extract parameters
        N = data.get('N')
        P = data.get('P')
        K = data.get('K')
        temperature = data.get('temperature')
        humidity = data.get('humidity')
        ph = data.get('ph')
        rainfall = data.get('rainfall')
        
        # Validate that all parameters are provided
        if None in [N, P, K, temperature, humidity, ph, rainfall]:
            return jsonify({'error': 'Missing required parameters'}), 400
        
        # Get prediction from model
        predicted_crop = predict_crop(N, P, K, temperature, humidity, ph, rainfall)
        
        # Return prediction as JSON
        return jsonify({'crop': predicted_crop})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
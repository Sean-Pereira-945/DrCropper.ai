# TODO: Replace this placeholder with a real machine learning model loaded from a .pkl file.

def predict_crop(N, P, K, temperature, humidity, ph, rainfall):
    """
    Placeholder function for crop prediction.
    
    Parameters:
    - N: Nitrogen content in soil
    - P: Phosphorus content in soil
    - K: Potassium content in soil
    - temperature: Temperature in Celsius
    - humidity: Humidity percentage
    - ph: pH value of soil
    - rainfall: Rainfall in mm
    
    Returns:
    - String: Predicted crop name
    """
    
    # Simple rule-based logic to simulate ML prediction
    if rainfall > 200 and P > 50:
        return 'Rice'
    elif temperature > 25 and humidity < 60:
        return 'Maize'
    elif K > 200 and N > 100:
        return 'Grapes'
    elif ph > 7 and temperature < 20:
        return 'Apple'
    elif humidity > 80 and temperature > 20:
        return 'Cotton'
    elif N > 80 and P > 40:
        return 'Sugarcane'
    elif temperature < 25 and rainfall < 100:
        return 'Barley'
    else:
        return 'Wheat'  # Default crop
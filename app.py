from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_KEY = 'f83e477c2e254a9a584a486e7ea3ae1f'  # Replace with your OpenWeatherMap API key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    units = request.args.get('units', 'metric')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={units}'
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({'error': 'City not found'}), 404

    data = response.json()
    weather = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'wind_speed': data['wind']['speed'],
        'icon': data['weather'][0]['icon']
    }
    return jsonify(weather)

if __name__ == '__main__':
    app.run(debug=True)

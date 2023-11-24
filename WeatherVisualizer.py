import requests
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/weather-chart')
def weather_chart():
    api_key = 'cd2e63c3c1fc41a9af6102958221307'
    api_url = 'http://api.weatherapi.com/v1/current.json?key=cd2e63c3c1fc41a9af6102958221307&q=Kyiv&aqi=no'

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }

    try:
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            data = response.json()

            # Извлечение данных для визуализации
            temperature_c = data['current']['temp_c']
            feelslike_c = data['current']['feelslike_c']

            # Подготовка данных для диаграммы
            labels = ['Temp', 'feels like']
            values = [temperature_c, feelslike_c]
            colors = ['blue', 'red']

            return jsonify({'labels': labels, 'values': values, 'colors': colors})

        else:
            return jsonify({'error': f'Ошибка запроса: {response.status_code}, {response.text}'})

    except Exception as e:
        return jsonify({'error': f'Произошла ошибка: {e}'})

if __name__ == '__main__':
    app.run(debug=True)

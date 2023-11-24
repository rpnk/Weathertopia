import matplotlib.pyplot as plt
import requests

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

        # Извлечение данных для визуализации (пример: температура)
        temperature_c = data['current']['temp_c']
        feelslike_c = data['current']['feelslike_c']

        # Визуализация
        labels = ['Макс лох', 'Макс крутой']
        values = [temperature_c, feelslike_c]

        colors = ['blue', 'red']  # Specify colors for each bar

        plt.bar(labels, values, color=colors)
        plt.title('Температура в Киеве')
        plt.xlabel('Показатель')
        plt.ylabel('Температура (°C)')
        plt.show()

    else:
        print(f'Ошибка запроса: {response.status_code}, {response.text}')

except Exception as e:
    print(f'Произошла ошибка: {e}')

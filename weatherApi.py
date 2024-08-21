import requests
from decouple import config

def weatherApi(city: str):
    print(f"Fetching weather data for city: {city}")
    api_key = config('WEATHER_API_KEY')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        print(f"Weather data for {city}: temp={temp}, humidity={humidity}, description={description}")
        return temp, humidity, description
    else:
        error_message = data.get('message', 'Unknown error')
        print(f"Error fetching weather data: {error_message}")
        raise Exception(f"Error fetching weather data: {error_message}")

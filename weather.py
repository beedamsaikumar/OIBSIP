import requests

def get_weather_data(location):
    api_key = '7488c4dd1753a9220280b651c78bdecc'  # Replace with your API key from OpenWeatherMap
    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    try:
        response = requests.get(base_url, params={'q': location, 'appid': api_key, 'units': 'metric'})
        if response.status_code == 200:
            weather_data = response.json()
            return weather_data
        else:
            return None
    except requests.RequestException as e:
        print(f"Request Exception: {e}")
        return None

def display_weather(weather_data):
    if weather_data is None:
        print("Failed to fetch weather data. Please check your input.")
        return

    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    description = weather_data['weather'][0]['description']

    print(f"Weather in {weather_data['name']}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description.capitalize()}")

if __name__ == "__main__":
    location = input("Enter city name or ZIP code: ")
    weather_info = get_weather_data(location)

    display_weather(weather_info)

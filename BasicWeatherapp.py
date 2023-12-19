import requests

def get_weather_data(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": str(location),  # Convert input to string
        "appid": api_key,
        "units": "metric"  # Change units as needed (metric/imperial)
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather_desc = data["weather"][0]["description"]
            
            print(f"Weather in {location}:")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Weather: {weather_desc}")
        else:
            print("Failed to fetch weather data.")
    except requests.RequestException as e:
        print(f"Error: {e}")

def main():
    api_key = "7488c4dd1753a9220280b651c78bdecc"  # Replace with your API key
    location = input("Enter city name or ZIP code: ")

    get_weather_data(api_key, location)

if __name__ == "__main__":
    main()



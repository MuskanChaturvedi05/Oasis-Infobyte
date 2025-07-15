import requests

def get_weather(city, api_key):
    API_Key = '4ab421cfc1eedb9a03dbdeb1030a4dc4'
    base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=metric'

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        weather = data['weather'][0]['description'].title()
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        print(f"\nWeather in {city.title()}:")
        print(f"Condition  : {weather}")
        print(f"Temperature: {temperature}°C (Feels like {feels_like}°C)")
        print(f"Humidity   : {humidity}%")
        print(f"Wind Speed : {wind_speed} m/s\n")
    else:
        print(f"Error: {data.get('message', 'Unable to fetch weather data')}")

if __name__ == "__main__":
    print("=== Weather App ===")
    city_name = input("Enter city name: ")
    api_key = input("Enter your OpenWeatherMap API key: ")
    get_weather(city_name, api_key)

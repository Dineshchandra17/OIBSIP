import requests # type: ignore

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={location}&appid={api_key}&units=metric"
    
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        
        temperature = main["temp"]
        humidity = main["humidity"]
        description = weather["description"]
        
        print(f"Weather in {location}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {description.capitalize()}")
    else:
        print(f"City {location} not found.")

def main():
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    location = input("Enter city name: ")
    get_weather(api_key, location)

if __name__ == "__main__":
    main()
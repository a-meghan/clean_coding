class WeatherData:
    def __init__(self, city):
        self.city = city
        self.data = self.fetch_weather_data()

    def fetch_weather_data(self):
        # Simulated function to fetch weather data for a given city
        print(f"Fetching weather data for {self.city}...")
        # Simulated data based on city
        weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
        }
        return weather_data.get(self.city, {})

    def parse_weather_data(self):
        if not self.data:
            return "Weather data not available"
        temperature = self.data["temperature"]
        condition = self.data["condition"]
        humidity = self.data["humidity"]
        return f"Weather in {self.city}: {temperature} degrees, {condition}, Humidity: {humidity}%"
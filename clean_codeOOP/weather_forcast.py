from weather_data import WeatherData

class WeatherForecast:
    def __init__(self, city, detailed=False):
        self.city = city
        self.detailed = detailed
        self.weather_data = WeatherData(city)

    def get_forecast(self):
        if self.detailed:
            return self.weather_data.parse_weather_data()
        else:
            return f"Weather in {self.city}: {self.weather_data.data['temperature']} degrees, {self.weather_data.data['condition']}"
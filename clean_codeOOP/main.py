from weather_forcast import WeatherForecast

def main():
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        forecast = WeatherForecast(city, detailed == 'yes')
        print(forecast.get_forecast())
  
if __name__ == "__main__":  
    main()
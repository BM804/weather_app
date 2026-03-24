import requests

# Your API URL NO api key needed
URL = "https://api.open-meteo.com/v1/forecast?latitude=22.5626&longitude=88.363&hourly=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m&timezone=auto"

def get_weather():
    try:
        response = requests.get(URL)
        data = response.json()

        # Get first hour data
        temp = data["hourly"]["temperature_2m"][0]
        humidity = data["hourly"]["relative_humidity_2m"][0]
        wind = data["hourly"]["wind_speed_10m"][0]

        print("\n📍 Location: Kolkata")
        print(f"🌡️ Temperature: {temp}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌬️ Wind Speed: {wind} km/h")

    except Exception as e:
        print("Error fetching data:", e)


def main():
    print("🌦️ WEATHER APP (BM804)")

    while True:
        choice = input("\nPress Enter to get weather or type 'e': ")

        if choice.lower() == "e":
            print("Exiting app...Dhonnobad")
            break

        get_weather()


if __name__ == "__main__":
    main()

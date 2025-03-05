import requests

OPENWEATHERMAP_KEY = "2f44ab8d94825710392977b37c24d3ac"
OPENWEATHERMAP_FORMAT_URL = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

def print_weather(city: str) -> None:
    response = requests.get(OPENWEATHERMAP_FORMAT_URL.format(city=city, key=OPENWEATHERMAP_KEY))
    if response.status_code != 200:
        raise RuntimeError(f"Request to OpenWeatherMap failed with status code {response.status_code}")
    data = response.json()
    print(f"Weather forecast for {city}:")
    print(f"    Sky:         {data['weather'][0]['main'].rjust(10)}")
    print(f"    Temperature: {round(data['main']['temp'] - 273.15):7} \u2103")
    print(f"    Humidity:    {data['main']['humidity']:7}  %")
    print(f"    Pressure:    {data['main']['pressure']:7} Па")


# noinspection HttpUrlsUsage
OPEN_NOTIFY_POSITION_URL = "http://api.open-notify.org/iss-now.json"
# noinspection HttpUrlsUsage
OPEN_NOTIFY_PEOPLES_URL = "http://api.open-notify.org/astros.json"

def print_iss_data():
    response1 = requests.get(OPEN_NOTIFY_POSITION_URL)
    response2 = requests.get(OPEN_NOTIFY_PEOPLES_URL)
    if response1.status_code != 200 or response2.status_code != 200:
        raise RuntimeError(
            f"Request to open-notify failed with status codes {response1.status_code}, {response2.status_code}"
        )
    lat, lon = response1.json()["iss_position"].values()
    peoples = [i["name"] for i in response2.json()["people"] if i["craft"] == "ISS"]
    print("ISS position:")
    print(f"    Latitude:  {float(lat):10.6f}\u00B0")
    print(f"    Longitude: {float(lon):10.6f}\u00B0")
    print()
    print("Peoples in ISS:")
    for people in peoples:
        parts = people.split()
        print(f"    " + "".join(part.ljust(15) for part in parts))


if __name__ == '__main__':
    print_weather(city="London")
    print("\n")
    print_iss_data()

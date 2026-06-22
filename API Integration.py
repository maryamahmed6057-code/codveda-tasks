import requests
def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        current = data["current_condition"][0]

        temp = current["temp_C"]
        humidity = current["humidity"]
        wind_speed = current["windspeedKmph"]
        weather = current["weatherDesc"][0]["value"]


        print("\n========== Weather Information ==========")
        print(f"City: {city.title()}")
        print(f"Temperature: {temp} °C")
        print(f"Weather: {weather}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} km/h")
        print("=========================================")

    except requests.exceptions.HTTPError:
        print("HTTP Error: Unable to retrieve data.")

    except requests.exceptions.ConnectionError:
        print("Connection Error: Check your internet connection.")

    except requests.exceptions.Timeout:
        print("Request Timeout.")

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

    except KeyError:
        print("Unexpected response from the API.")

city = input("Enter city name: ")
get_weather(city)

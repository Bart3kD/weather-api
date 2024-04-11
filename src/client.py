import requests
from api_key import key
import controllers as controllers


def fetch_air_quality_data():
    r = requests.get("http://api.airvisual.com/v2/city?city=Warsaw&state=Mazovia&country=Poland&key=" + key).json()

    data = {"pollution": r['data']['current']['pollution'], "weather": r['data']['current']['weather']}

    response = requests.post(url="http://127.0.0.1:5001/airQualities", json=data,
                             headers={"Content-Type": "application/json"})

    if response.status_code == 201:
        print("AirQuality created successfully!")
    else:
        print("Failed to create AirQuality.")
        print(response.text)

    controllers.CreateAirQualityController(controllers.AirQualityRepository(), controllers.AirQuality()).create(data)

    return data


print(fetch_air_quality_data())
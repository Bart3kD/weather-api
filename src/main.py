from flask import Flask, Response
from api_key import key
import requests
import json

from controllers import create_airQuality_controller, get_airQualities_controller

app = Flask(__name__)

r = requests.get("http://api.airvisual.com/v2/city?city=Warsaw&state=Mazovia&country=Poland&key=" + key).json()

data = r['data']
current = data['current']
pollution = current['pollution']
weather = current['weather']


@app.get('/')
def ping():
    return 'Welcome to the AirQuality API!'


@app.get('/airQualities')
def get_airQualities() -> Response:
    airQualities = get_airQualities_controller.get()
    return Response(response=json.dumps(airQualities), status=200, mimetype="application/json")


@app.get('/airQualities/create')
def create_airQuality() -> Response:
    try:
        create_airQuality_controller.create({"pollution": pollution, "weather": weather})
        return Response(response="AirQuality created", status=201)
    except ValueError as error:
        return Response(response=str(error), status=400)
    

@app.get('/airQualities/<string:timestamp>')
def get_airQuality(timestamp: str) -> Response:
    try:
        airQuality = get_airQualities_controller.get(timestamp=timestamp)
        return Response(response=json.dumps(airQuality), status=200, mimetype="application/json")
    except ValueError as error:
        return Response(response=str(error), status=400)





app.run(port=5001, debug=True)
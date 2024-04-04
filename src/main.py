from flask import Flask, Response
from api_key import key
import requests
import json

from controllers import create_airQuality_controller, get_airQualities_controller

app = Flask(__name__)

r = requests.get("http://api.airvisual.com/v2/city?city=Warsaw&state=Mazovia&country=Poland&key=" + key)
r_json = r.json()

data = r_json['data']
current = data['current']
pollution = current['pollution']
weather = current['weather']


@app.get('/ping')
def ping() -> str:
    return 'pong'


@app.get('/airQualities')
def get_airQualities() -> Response:
    airQualities = get_airQualities_controller.get()
    return Response(response=json.dumps(airQualities), status=200, mimetype="application/json")


@app.get('/airQualities/<str:timestamp>')
def get_airQuality(timestamp: str) -> Response:
    try:
        airQuality = get_airQualities_controller.get(timestamp=timestamp)
        return Response(response=json.dumps(airQuality), status=200, mimetype="application/json")
    except ValueError as error:
        return Response(response=str(error), status=400)



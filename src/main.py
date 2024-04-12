from flask import Flask, Response, jsonify, request
import json
from controllers import CreateAirQualityController, GetAirQualitiesController
from airQuality import AirQuality
from repositories import AirQualityRepository

app = Flask(__name__)


class AirQualityAPI:
    def __init__(self, dto: AirQuality, repository: AirQualityRepository, createController: CreateAirQualityController, getController: GetAirQualitiesController):
        self.air_quality = repository()
        self.createController = createController(self.air_quality, dto())
        self.getController = getController(self.air_quality)


    def ping(self):
        return 'Welcome to the AirQuality API!'

    def get_airQualities(self):
        air_qualities = GetAirQualitiesController.get(air_quality_api.getController)
        return Response(response=json.dumps(air_qualities), status=200, mimetype="application/json")

    def get_airQuality_by_timestamp(self, timestamp):
        try:
            air_quality = self.getController.get(timestamp=timestamp)
            return Response(response=json.dumps(air_quality), status=200, mimetype="application/json")
        except ValueError as error:
            return Response(response=str(error), status=400)


air_quality_api = AirQualityAPI(AirQuality, AirQualityRepository, CreateAirQualityController, GetAirQualitiesController)


@app.route('/')
def ping():
    return air_quality_api.ping()


@app.route('/airQualities', methods=['GET'])
def get_airQualities():
    return air_quality_api.get_airQualities()


@app.route('/airQualities', methods=['POST'])
def create_airQuality():
    data = request.json
    data = air_quality_api.createController.create(data)
    return jsonify(data), 201


@app.route('/airQualities/<string:timestamp>', methods=['GET'])
def get_airQuality(timestamp):
    return air_quality_api.get_airQuality_by_timestamp(timestamp)


if __name__ == "__main__":
    app.run(port=5001, debug=True)
import datetime
import copy

from src.repositories import AirQualityRepository, airQualityRepository

from src.airQuality import AirQuality, airQuality


class CreateAirQualityController:
    def __init__(self, repository: AirQualityRepository, dto: AirQuality) -> None:
        self._repository = repository
        self.dto = dto

    
    def create(self, airQuality: dict[str, str | int | float]) -> None:
        self._dto.add_data(airQuality)
        data = self._dto.get_data()

        if None in data:
            raise ValueError("Missing one of the arguments")

        timestamp = data[0]
        aqi_US = data[1]
        aqi_China = data[2]
        main_pollutant_US = data[3]
        main_pollutant_China = data[4]
        temperature = data[5]
        athmospheric_pressure = data[6]
        humidity = data[7]
        wind_speed = data[8]
        wind_direction = data[9]

        self._repository.add_airQuality(timestamp, aqi_US, aqi_China, main_pollutant_US, main_pollutant_China, temperature, athmospheric_pressure, humidity, wind_speed, wind_direction)
    

class GetAirQualitiesController:
    def __init__(self, repository: AirQualityRepository, dto: AirQuality) -> None:
        self._repository = repository
        self.dto = dto
    
    def get(self, timestamp: str | None = None):
        airQualities = copy.deepcopy(self._repository.get_airQualities())
        if timestamp is None:
            return airQualities

        for airQuality in airQualities:
            if airQuality['timestamp'] == timestamp:
                return airQuality
        
        raise ValueError('Invalid timestamp')

create_airQuality_controller = CreateAirQualityController(airQualityRepository, airQuality)
get_airQualities_controller = GetAirQualitiesController(airQualityRepository)
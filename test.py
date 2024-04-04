import requests
import copy

class AirQuality:
    def __init__(self):
        self._timestamp = None
        self._aqi_US = None
        self._aqi_China = None
        self._main_pollutant_US = None
        self._main_pollutant_China = None
        self._temperature = None
        self._athmospheric_pressure = None
        self._humidity = None
        self._wind_speed = None
        self._wind_direction = None


    def add_data(self, data: dict[str, None | dict[str, float | int | str]]):
        for key in list(data.keys()):
            if key not in ['pollution', 'weather']:
                raise ValueError("Invalid airQuality data")
        
        for key in [key for key in ["pollution", "weather"] if key not in list(data.keys())]:
            data[key] = None
        
        pollution = data['pollution']
        weather = data['weather']

        timestamp = pollution['ts']
        aqi_US = pollution['aqius']
        aqi_China = pollution['aqicn']
        main_pollutant_US = pollution['mainus']
        main_pollutant_China = pollution['maincn']
        temerature = weather['tp']
        athmospheric_pressure = weather['pr']
        humidity = weather['hu']
        wind_speed = weather['ws']
        wind_direction = weather['wd']

        self._timestamp = timestamp
        self._aqi_US = aqi_US
        self._aqi_China = aqi_China
        self._main_pollutant_US = main_pollutant_US
        self._main_pollutant_China = main_pollutant_China
        self._temperature = temerature
        self._athmospheric_pressure = athmospheric_pressure
        self._humidity = humidity
        self._wind_speed = wind_speed
        self._wind_direction = wind_direction
    
    def get_data(self) -> tuple[str, int, int, str, str, int, int, int, float, int]:
        data = (self._timestamp, self._aqi_US, self._aqi_China, self._main_pollutant_US, self._main_pollutant_China, self._temperature, self._athmospheric_pressure, self._humidity, self._wind_speed, self._wind_direction)
        self._timestamp = None
        self._aqi_US = None
        self._aqi_China = None
        self._main_pollutant_US = None
        self._main_pollutant_China = None
        self._temperature = None
        self._athmospheric_pressure = None
        self._humidity = None
        self._wind_speed = None
        self._wind_direction = None
        return data

airQuality = AirQuality()

class AirQualityRepository:
    def __init__(self) -> None:
        self._airQualities: list[dict[str, str | int| float]] = []
    

    def add_airQuality(self, 
                        timestamp: str,
                        aqi_US: int,
                        aqi_China: int,
                        main_pollutant_US: str,
                        main_pollutant_China: str,
                        temperature: int,
                        athmospheric_pressure: int,
                        humidity: int,
                        wind_speed: float,
                        wind_direction: int
                       ) -> None:
        self._airQualities.append(
            {
                'timestamp': timestamp,
                'aqi_US': aqi_US,
                'aqi_China': aqi_China,
                'main_pollutant_US': main_pollutant_US,
                'main_pollutant_China': main_pollutant_China,
                'temperature': temperature,
                'athmospheric_pressure': athmospheric_pressure,
                'humidity': humidity,
                'wind_speed': wind_speed,
                'wind_direction': wind_direction
            }
        )

    
    def get_airQualities(self) -> list[dict[str, str | int| float]]:
        return self._airQualities

airQualityRepository = AirQualityRepository()


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
    def __init__(self, repository: AirQualityRepository) -> None:
        self._repository = repository
    
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


r = requests.get("http://api.airvisual.com/v2/city?city=Warsaw&state=Mazovia&country=Poland&key=c022051a-4802-44bd-8cf2-5e10d3bfa30f")
r_json = r.json()

data = r_json['data']
current = data['current']
pollution = current['pollution']
weather = current['weather']

airQuality.add_data({
    "pollution": pollution,
    "weather": weather,
})

dataToRepository = airQuality.get_data()

timestamp = dataToRepository[0]
aqi_US = dataToRepository[1]
aqi_China = dataToRepository[2]
main_pollutant_US = dataToRepository[3]
main_pollutant_China = dataToRepository[4]
temperature = dataToRepository[5]
athmospheric_pressure = dataToRepository[6]
humidity = dataToRepository[7]
wind_speed = dataToRepository[8]
wind_direction = dataToRepository[9]

airQualityRepository.add_airQuality(timestamp, aqi_US, aqi_China, main_pollutant_US, main_pollutant_China, temperature, athmospheric_pressure, humidity, wind_speed, wind_direction)

print(get_airQualities_controller.get())
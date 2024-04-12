from pydantic import BaseModel, field_validator
from typing import Optional


class AirQuality(BaseModel):
    _timestamp: Optional[str]
    _aqi_US: Optional[int]
    _aqi_China: Optional[int]
    _main_pollutant_US: Optional[str]
    _main_pollutant_China: Optional[str]
    _temperature: Optional[int]
    _atmospheric_pressure: Optional[int]
    _humidity: Optional[int]
    _wind_speed: Optional[float]
    _wind_direction: Optional[int]

    @classmethod
    @field_validator("_timestamp")
    def validate_timestamp(cls, value):
        return value

    @classmethod
    @field_validator("_aqi_US")
    def validate_aqi_us(cls, value):
        if value is not None and (value < 0 or value > 500):
            raise ValueError("AQI_US must be between 0 and 500")
        return value

    @classmethod
    @field_validator("_aqi_China")
    def validate_aqi_china(cls, value):
        if value is not None and (value < 0 or value > 500):
            raise ValueError("AQI_China must be between 0 and 500")
        return value

    @classmethod
    @field_validator("_main_pollutant_US", "_main_pollutant_China")
    def validate_pollutants(cls, values):
        return values

    @classmethod
    @field_validator("_temperature", "_atmospheric_pressure", "_humidity")
    def validate_weather_values(cls, values):
        for value in values:
            if value is not None and value < 0:
                raise ValueError("Temperature, pressure, and humidity cannot be negative")
        return values

    @classmethod
    @field_validator("_wind_speed")
    def validate_wind_speed(cls, value):
        if value is not None and value < 0:
            raise ValueError("Wind speed cannot be negative")
        return value

    def add_data(self, data: dict[str, Optional[dict[str, Optional[float]]]]):
        for key in ['pollution', 'weather']:
            if key not in data:
                data[key] = None

        pollution_data = data.get('pollution', {})
        weather_data = data.get('weather', {})

        self._timestamp = pollution_data.get('ts')
        self._aqi_US = pollution_data.get('aqius')
        self._aqi_China = pollution_data.get('aqicn')
        self._main_pollutant_US = pollution_data.get('mainus')
        self._main_pollutant_China = pollution_data.get('maincn')
        self._temperature = weather_data.get('tp')
        self._atmospheric_pressure = weather_data.get('pr')
        self._humidity = weather_data.get('hu')
        self._wind_speed = weather_data.get('ws')
        self._wind_direction = weather_data.get('wd')

    def get_data(self) -> tuple[str, int, int, str, str, int, int, int, float, int]:
        data = (
            self._timestamp, self._aqi_US, self._aqi_China, self._main_pollutant_US, self._main_pollutant_China,
            self._temperature, self._atmospheric_pressure, self._humidity, self._wind_speed, self._wind_direction
        )
        return data
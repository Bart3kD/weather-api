from pydantic import BaseModel
from typing import Optional


class AirQuality(BaseModel):
    timestamp: Optional[str]
    aqi_US: Optional[int]
    aqi_China: Optional[int]
    main_pollutant_US: Optional[str]
    main_pollutant_China: Optional[str]
    temperature: Optional[int]
    atmospheric_pressure: Optional[int]
    humidity: Optional[int]
    wind_speed: Optional[float]
    wind_direction: Optional[int]

    def add_data(self, data: dict[str, Optional[dict[str, Optional[float]]]]):
        for key in ['pollution', 'weather']:
            if key not in data:
                data[key] = None

        self.timestamp = data['pollution'].get('ts')
        self.aqi_US = data['pollution'].get('aqius')
        self.aqi_China = data['pollution'].get('aqicn')
        self.main_pollutant_US = data['pollution'].get('mainus')
        self.main_pollutant_China = data['pollution'].get('maincn')
        self.temperature = data['weather'].get('tp')
        self.atmospheric_pressure = data['weather'].get('pr')
        self.humidity = data['weather'].get('hu')
        self.wind_speed = data['weather'].get('ws')
        self.wind_direction = data['weather'].get('wd')
        
        if self.temperature >= 100 or self.temperature <= -100:
             raise ValueError('Invalid temperature')
        if self.atmospheric_pressure >= 2000 or self.atmospheric_pressure <= 500:
             raise ValueError('Invalid athmospheric pressure')

    def get_data(self) -> tuple[str, int, int, str, str, int, int, int, float, int]:
        data = (
            self.timestamp, self.aqi_US, self.aqi_China, self.main_pollutant_US, self.main_pollutant_China,
            self.temperature, self.atmospheric_pressure, self.humidity, self.wind_speed, self.wind_direction
        )
        self.timestamp = None
        self.aqi_US = None
        self.aqi_China = None
        self.main_pollutant_US = None
        self.main_pollutant_China = None
        self.temperature = None
        self.atmospheric_pressure = None
        self.humidity = None
        self.wind_speed = None
        self.wind_direction = None
        return data

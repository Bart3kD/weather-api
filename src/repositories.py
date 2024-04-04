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

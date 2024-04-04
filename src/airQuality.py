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

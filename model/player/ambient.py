from numstat import NumStat

class Ambient:
    def __init__(self):
        self.temperature = NumStat(0)
        self.weather = None
        self.earthquake_intensity = NumStat(0)
        self.volcanism_intensity = NumStat(0)
        self.wind_speed = NumStat(0)
        self.wind_strength = NumStat(0)
        self.radiation = NumStat(0)
        self.air_corrosion = NumStat(0)
        self.tides = NumStat(0)
        self.uv_index = NumStat(0)
        self.sunlight = NumStat(100)
        self.clouds = NumStat(100)
        self.sun_event = None
        self.inner_moon = None
        self.outer_moon = None
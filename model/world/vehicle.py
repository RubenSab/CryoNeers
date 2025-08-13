from model.items.storage import Storage
from model.numstat import NumStat
from model.items.air_tank import AirTank


class Vehicle:
    def __init__(self):
        self.crew = None
        self.air_tank = AirTank(6)
        self.storage = Storage(8)
        self.hull_integrity = NumStat(100)
        self.solar_panels = NumStat(100)
        self.warming_systems = NumStat(100)
from Model.player.storage import Storage
from numstat import NumStat


class Vehicle:
    def __init__(self):
        self.crew = None
        self.air_tank = None
        self.storage = Storage()
        self.hull_integrity = NumStat(100)
        self.solar_panels = NumStat(100)
        self.warming_systems = NumStat(100)
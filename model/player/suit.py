from model.numstat import NumStat
from model.items.air_tank import AirTank

class Suit:
    def __init__(self):
        self.battery = NumStat(100)
        self.integrity = NumStat(100)
        self.air_tank = AirTank()
        self.terrain_grip = NumStat(100)
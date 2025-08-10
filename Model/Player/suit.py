from Model.numstat import NumStat

class Suit:
    def __init__(self):
        self.battery = NumStat(100)
        self.integrity = NumStat(100)
        self.air_tank = None
        self.terrain_grip = NumStat(100)
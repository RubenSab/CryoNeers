from model.numstat import NumStat


class EnergySource:
    def __init__(self):
        self.integrity = NumStat(100)
        self.heating_regulation = NumStat(100)
        self.battery_slots = []
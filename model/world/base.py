from model.numstat import NumStat


class Base:
    def __init__(self):
        self.crew = None
        self.rooms = {
            # add rooms each with a storage
        }
        self.air_tank = None
        self.hull_integrity = NumStat(100)
        self.solar_panels = NumStat(100)
        self.warming_systems = NumStat(100)
        self.foundations = None
        self.floaters = None
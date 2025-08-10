from suit import Suit
from handheld import Handheld
from storage import Storage
from Model.numstat import NumStat

class Player:
    def __init__(self):
        self.stats = {
            'health': NumStat(100),
            'hunger': NumStat(0),
            'fatigue': NumStat(0),
            'morale': NumStat(100),
        }
        self.suit = Suit()
        self.handheld = Handheld()
        self.storage = Storage()
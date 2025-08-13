from model.player.map import Map
from model.items.notes import Notes

class Handheld:
    def __init__(self):
        self.notes = Notes()
        self.map = Map()

    # TODO
    def interact(self):
        pass
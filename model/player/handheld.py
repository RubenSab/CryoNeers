from model.singletons.map_instance import map
from model.singletons.notes_instance import notes

class Handheld:
    def __init__(self):
        self.notes = notes
        self.map = map

    # TODO
    def interact(self):
        pass
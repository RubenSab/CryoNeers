from model.model import clock
from map import Map


class Handheld:
    def __init__(self):
        self.clock = clock
        self.game_notes = []
        self.player_notes = []
        self.map = Map()

    def add_player_note(self, content):
        self.player_notes.append({
            'content': content,
            'date': clock.date_str()
        })

    def remove_player_note(self, index):
        self.player_notes.pop(index)

    def add_game_note(self, content):
        self.player_notes.append({
            'content': content,
            'date': clock.date_str()
        })

    # TODO
    def interact(self):
        pass
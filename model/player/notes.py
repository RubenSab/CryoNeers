from model.singletons.clock_instance import clock
from model.constants import PLAYER_NAME

class Notes:
    def __init__(self):
        self.archive = []

    def add_player_note(self, title, content):
        self.archive.append({
            'title': title,
            'content': content,
            'date': clock.date_str(compact = True),
            'author': PLAYER_NAME,
        })

    def remove_player_note(self, index):
        if self.archive[index]['author'] == PLAYER_NAME:
            self.archive.pop(index)

    def add_game_note(self, title, content, sender, date=None):
        if date is None:
            date = clock.date_str(compact=True)
        self.archive.append({
            'title': title,
            'content': content,
            'date': date,
            'author': sender
        })

    def __str__(self):
        return '\n'.join(reversed([
            f'[{note["date"]}][{note['author']}]: {note["title"]}'
            for note in self.archive
        ]))

    # TODO
    def interact(self):
        pass
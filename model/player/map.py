from model.singletons.notes_instance import notes
import math


MAP_HEIGHT = 21
ASPECT_RATIO = 2.5
MAP_WIDTH = int(MAP_HEIGHT*ASPECT_RATIO)
HIGHLIGHT_CHAR = '◇'


def coords_to_index(x, y):
    return x+MAP_WIDTH//2, y+MAP_HEIGHT//2


class Map:
    def __init__(self):
        self.matrix = [[{
            'symbol': ' ',
            'note': ' '
        } for _ in range(MAP_WIDTH)] for __ in range(MAP_HEIGHT)]
        self.highlighted_cell = None

    def mark_cell(self, x, y, char, note):
        x, y = coords_to_index(x, y)
        if 0 <= x < MAP_WIDTH and 0 <= y < MAP_HEIGHT and len(str(char)) == 1:
            self.matrix[y][x] = {
                'symbol': char,
                'note': note
            }
            notes.add_player_note(f'description of point [{char}] on map', note)

    def get_cell(self, x, y):
        x, y = coords_to_index(x, y)
        return self.matrix[y][x]

    def interact(self):
        pass

    def highlight_cell(self, x, y):
        self.highlighted_cell = (x, y)

    def get_distance_from_base(self, x, y):
        return math.sqrt(x**2 + y**2)

    def __str__(self):
        # Translate highlighted cell once for rendering
        if self.highlighted_cell is not None:
            highlight_x, highlight_y = coords_to_index(*self.highlighted_cell)
        else:
            highlight_x, highlight_y = None, None

        lines = '\n'.join([
            '│' + ''.join(
                [HIGHLIGHT_CHAR if (c, r) == (highlight_x, highlight_y) else cell['symbol']
                 for c, cell in enumerate(row)]
            ) + '│'
            for r, row in enumerate(self.matrix)
        ])

        upper_frame = '┌' + '─' * MAP_WIDTH + '┐\n'
        lower_frame = '\n└' + '─' * MAP_WIDTH + '┘\n'

        if self.highlighted_cell is not None:
            cell = self.get_cell(*self.highlighted_cell)  # get_cell will translate coords
            symbol = cell["symbol"] if cell["symbol"] != ' ' else HIGHLIGHT_CHAR
            note = cell["note"] if cell["note"] != ' ' else 'No description'
            note = f'[{symbol}] {note}'
            distance_from_base = (
                f' [{self.get_distance_from_base(*self.highlighted_cell):.2f}'
                f' Km away from base]'
            )
        else:
            note = '[ ] Highlight position to view description'
            distance_from_base = ''
        return upper_frame + lines + lower_frame + note + distance_from_base
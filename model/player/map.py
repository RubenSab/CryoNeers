MAP_HEIGHT = 20
ASPECT_RATIO = 2.5
MAP_WIDTH = int(MAP_HEIGHT*ASPECT_RATIO)
HIGHLIGHT_CHAR = '◇'

class Map:
    def __init__(self):
        self.matrix = [[{
            'symbol': ' ',
            'note': ' '
        } for _ in range(MAP_WIDTH)] for __ in range(MAP_HEIGHT)]
        self.highlighted_cell = None

    def highlight_cell(self, x, y):
        self.highlighted_cell = (x, y)

    def __str__(self):
        lines = '\n'.join([
            '│' + ''.join(
                [HIGHLIGHT_CHAR if (c, r) == self.highlighted_cell else cell['symbol']
                 for c, cell in enumerate(row)]
            ) + '│'
            for r, row in enumerate(self.matrix)
        ])
        upper_frame = '┌' + '─' * MAP_WIDTH + '┐\n'
        lower_frame = '\n└' + '─' * MAP_WIDTH + '┘\n'
        if self.highlighted_cell is not None:
            cell = self.get_cell(*self.highlighted_cell)
            symbol = cell["symbol"] if cell["symbol"] != ' ' else HIGHLIGHT_CHAR
            note = cell["note"] if cell["note"] != ' ' else 'No description'
            note = f'[{symbol}] {note}'
        else:
            note = '[ ] Highlight position to view description'
        return upper_frame + lines + lower_frame + note

    def mark_cell(self, x, y, char, note):
        if 0 <= x < MAP_WIDTH and 0 <= y < MAP_HEIGHT and len(str(char)) == 1:
            self.matrix[y][x] = {
                'symbol': char,
                'note': note
            }

    def get_cell(self, x, y):
        return self.matrix[y][x]

    # TODO
    def interact(self):
        pass
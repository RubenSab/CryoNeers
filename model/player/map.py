MAP_HEIGHT = 20
MAP_WIDTH = int(MAP_HEIGHT*3)

class Map:
    def __init__(self):
        self.matrix = [[(' ', "empty") for _ in range(MAP_WIDTH)] for __ in range(MAP_HEIGHT)]

    def __str__(self):
        lines = '\n'.join(['│'+''.join([i['symbol'] for i in row])+'│' for row in self.matrix])
        upper_frame = '┌'+'─'*MAP_WIDTH+'┐\n'
        lower_frame = '\n└'+'─'*MAP_WIDTH+'┘'
        return upper_frame + lines + lower_frame

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
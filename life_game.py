
def _get_terminal_size_windows():
    try:
        from ctypes import windll, create_string_buffer
        import struct

        # stdin handle is -10
        # stdout handle is -11
        # stderr handle is -12
        h = windll.kernel32.GetStdHandle(-12)
        csbi = create_string_buffer(22)
        res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
        if res:
            (bufx, bufy, curx, cury, wattr,
             left, top, right, bottom,
             maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
            sizex = right - left + 1
            sizey = bottom - top + 1
            return sizex, sizey
    except:
        pass


class Map:
    def __init__(self):
        x, y = _get_terminal_size_windows()

        self.x = int(x / 2)
        self.y = int(y - 2)

        self.map = []
        sub_map = [[0 for i in range(self.x)] for j in range(self.y)]

        self.map.append(sub_map)
        self.map.append(sub_map.copy())

        self.map_index = 0

    def get_around_cells(self, y, x):

        current_map = self.map[self.map_index]

        cell_count = 0
        if y - 1 >= 0:
            if current_map[y - 1][x] == 1:
                cell_count += 1

            if x - 1 >= 0:
                if current_map[y - 1][x - 1] == 1:
                    cell_count += 1

            if x + 1 < self.x:
                if current_map[y - 1][x + 1] == 1:
                    cell_count += 1

        if y + 1 < self.y:
            if current_map[y + 1][x] == 1:
                cell_count += 1

            if x - 1 >= 0:
                if current_map[y + 1][x - 1] == 1:
                    cell_count += 1

            if x + 1 < self.x:
                if current_map[y + 1][x + 1] == 1:
                    cell_count += 1

        if x - 1 >= 0:
            if current_map[y][x - 1] == 1:
                cell_count += 1

        if x + 1 < self.x:
            if current_map[y][x + 1] == 1:
                cell_count += 1

    def count(self):

        current_map = self.map[self.map_index]

        for y in range(self.y):
            for x in range(self.x):
                around_cells = self.get_around_cells(y, x)

                if current_map[y][x] == 1:
                    if 2 <= around_cells <= 3:
                        # alive
                        pass
                    elif around_cells < 2 or 3 < around_cells:
                        # death
                        pass
                else:
                    if around_cells == 3:
                        # new
                        pass

    def show(self):

        current_map = self.map[self.map_index]
        self.map_index += 1
        self.map_index %= 2

        print('')
        for y in range(self.y):
            for x in range(self.x):
                if current_map[y][x] == 0:
                    print('⚪', end='')
                else:
                    print('█', end='')


if __name__ == '__main__':
    map = Map()
    map.show()
    map.show()


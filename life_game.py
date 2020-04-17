import time


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
    def __init__(self, init_list=None):
        x, y = _get_terminal_size_windows()

        self.x = int(x / 2)
        self.y = int(y - 2)

        self.map = []
        sub_map1 = [[0 for i in range(self.x)] for j in range(self.y)]
        sub_map2 = [[0 for i in range(self.x)] for j in range(self.y)]

        self.map.append(sub_map1)
        self.map.append(sub_map2)

        self.map_index = 0

        if init_list is not None:
            for y, x in init_list:
                self.map[self.map_index][y][x] = 1

    def get_fixed_y(self, new_y):
        if new_y < 0:
            return self.y - 1
        elif new_y >= self.y:
            return 0
        return new_y

    def get_fixed_x(self, new_x):
        if new_x < 0:
            return self.x - 1
        elif new_x >= self.x:
            return 0
        return new_x

    def get_around_cells(self, last_map, y, x):
        check_list = [
            (self.get_fixed_y(y - 1), self.get_fixed_x(x - 1)),
            (self.get_fixed_y(y - 1), self.get_fixed_x(x)),
            (self.get_fixed_y(y - 1), self.get_fixed_x(x + 1)),
            (self.get_fixed_y(y), self.get_fixed_x(x - 1)),
            (self.get_fixed_y(y), self.get_fixed_x(x + 1)),
            (self.get_fixed_y(y + 1), self.get_fixed_x(x - 1)),
            (self.get_fixed_y(y + 1), self.get_fixed_x(x)),
            (self.get_fixed_y(y + 1), self.get_fixed_x(x + 1))
        ]

        cell_count = 0
        for current_y, current_x in check_list:
            if last_map[current_y][current_x] == 1:
                cell_count += 1

        return cell_count

    def count(self):

        last_map = self.map[self.map_index]
        self.map_index = (self.map_index + 1) % 2
        current_map = self.map[self.map_index]

        for y in range(self.y):
            for x in range(self.x):
                around_cells = self.get_around_cells(last_map, y, x)

                current_map[y][x] = 0
                if last_map[y][x] == 1:
                    if 2 <= around_cells <= 3:
                        current_map[y][x] = 1
                    elif around_cells < 2 or 3 < around_cells:
                        current_map[y][x] = 0
                else:
                    if around_cells == 3:
                        current_map[y][x] = 1

    def show(self, assign_map=None):
        if assign_map is None:
            current_map = self.map[self.map_index]
        else:
            current_map = assign_map
        print('')
        for y in range(self.y):
            for x in range(self.x):
                if current_map[y][x] == 0:
                    print('  ', end='')
                else:
                    print('█', end='')


if __name__ == '__main__':
    # https://zh.wikipedia.org/wiki/%E5%BA%B7%E5%A8%81%E7%94%9F%E5%91%BD%E6%B8%B8%E6%88%8F
    init_list = [
        # 信號燈
        (4, 5),
        (5, 5),
        (6, 5),
        # 蟾蜍
        (10, 10),
        (10, 11),
        (10, 12),
        (11, 9),
        (11, 10),
        (11, 11),
        # 脈衝星
        (10, 30),
        (11, 30),
        (12, 30),
        (12, 31),
        (10, 36),
        (11, 36),
        (12, 36),
        (12, 35),

        (14, 26),
        (14, 27),
        (14, 28),
        (15, 28),
        (20, 26),
        (20, 27),
        (20, 28),
        (19, 28),

        (14, 38),
        (14, 39),
        (14, 40),
        (15, 38),
        (20, 38),
        (20, 39),
        (20, 40),
        (19, 38),

        (22, 30),
        (23, 30),
        (24, 30),
        (22, 31),
        (22, 36),
        (23, 36),
        (24, 36),
        (22, 35),

        (18, 30),
        (19, 30),
        (18, 31),

        (14, 34),
        (15, 34),
        (14, 35),

        (14, 31),
        (14, 32),
        (15, 32),

        (18, 35),
        (18, 36),
        (19, 36),

        (19, 34),
        (20, 34),
        (20, 35),

        (15, 30),
        (16, 30),
        (16, 31),

        (19, 32),
        (20, 32),
        (20, 31),

        (15, 36),
        (16, 36),
        (16, 35),

        # 太空船
        (40, 0),
        (42, 0),
        (43, 1),
        (43, 2),
        (43, 3),
        (43, 4),
        (42, 4),
        (41, 4),
        (40, 3),

    ]

    map = Map(init_list)

    # map.show()
    # map.count()

    while True:
        map.show()
        map.count()
        time.sleep(0.1)

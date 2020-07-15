class Cell:
    # 1. find only one possible value
    # 2. if find, remove the value from relative line and jiugongge
    # 3. goto 1.

    OK = -1
    FIND = -2
    CONTRADICT = -3

    def __init__(self, map, y, x, value: int = 0):

        self.y = y
        self.x = x

        if value < 0 or 9 < value:
            raise ValueError('Cell value must in 0 ~ 9')

        self.value = value

        if value == 0:
            self.possible_value = [x for x in range(1, 10)]
        else:
            map.empty_cell -= 1
            self.possible_value = list()

    def __str__(self):
        if self.value == 0:
            return ' '
        return f'{self.value}'

    def remove_possible_value(self, map, value):
        if value in self.possible_value:
            self.possible_value.remove(value)
            if len(self.possible_value) == 1:
                self.value = self.possible_value[0]
                self.possible_value.clear()
                print(f'({self.y}, {self.x}) - find {self.value}')
                # return self.y, self.x, self.possible_value[0]

                map.empty_cell -= 1
                map.remove_possible_value(self)

                return self.FIND
            elif len(self.possible_value) == 0:
                return self.CONTRADICT
        return self.OK

    def set_value(self, value):
        if value not in self.possible_value:
            raise ValueError('It is impossible value')
        self.value = value
        self.possible_value.clear()


if __name__ == '__main__':
    c = Cell()
    print(c)
    for v in range(0, 10):
        c = Cell(v)
        print(c)

class Cell:
    OK = -1
    FIND = -2
    CONTRADICT = -3

    def __init__(self, sudoku, y, x, value: int = 0):

        self.y = y
        self.x = x

        if value < 0 or 9 < value:
            raise ValueError('Cell value must in 0 ~ 9')

        self.value = value

        if value == 0:
            self.possible_value = [x for x in range(1, 10)]
        else:
            sudoku.empty_cell -= 1
            self.possible_value = list()

    def __str__(self):
        if self.value == 0:
            return ' '
        return f'{self.value}'

    def remove_possible_value(self, value):
        if value in self.possible_value:
            self.possible_value.remove(value)
            if len(self.possible_value) == 1:
                return self.FIND
            if len(self.possible_value) == 0:
                return self.CONTRADICT
        return self.OK

    def set_value(self, sudoku, value):
        if value not in self.possible_value:
            print(self.value)
            print(self.possible_value)
            raise ValueError('It is impossible value')

        self.value = value
        self.possible_value.clear()

        sudoku.empty_cell -= 1


if __name__ == '__main__':
    c = Cell()
    print(c)
    for v in range(0, 10):
        c = Cell(v)
        print(c)

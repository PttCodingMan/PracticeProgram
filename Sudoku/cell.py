class Cell:
    def __init__(self, value: int = 0):

        if value < 0 or 9 < value:
            raise ValueError('Cell value must in 0 ~ 9')

        self.value = value

        if value == 0:
            self.possible_numbers = [x for x in range(1, 10)]
        else:
            self.possible_numbers = list()

    def __str__(self):
        if self.value == 0:
            return ' '
        return f'{self.value}'

    def show(self):
        print(self.__str__)


if __name__ == '__main__':
    c = Cell()
    print(c)
    for v in range(0, 10):
        c = Cell(v)
        print(c)


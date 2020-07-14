import util


class Line:
    def __init__(self, cell_list: list):
        util.check_value_count('Line', cell_list)

        self.cell_list = cell_list

    def __str__(self):
        buffer = '|'

        for cell in self.cell_list:
            buffer += f' {cell} |'

        return buffer


if __name__ == '__main__':

    from cell import Cell

    cell_list = list()
    for v in range(1, 10):
        cell_list.append(Cell(v))

    line = Line(cell_list)

    print(line)

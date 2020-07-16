from cell import Cell
import util


class Line:
    def __init__(self, cell_list: list):
        util.check_value_count('Line', cell_list)

        self.cell_list = cell_list

    def remove_possible_value(self, value):
        result = Cell.OK
        for cell in self.cell_list:
            remove_result = cell.remove_possible_value(value)
            if remove_result == Cell.CONTRADICT:
                return Cell.CONTRADICT
            if remove_result == Cell.FIND:
                result = Cell.FIND
        return result

    def __str__(self):
        buffer = '|'

        for cell in self.cell_list:
            buffer += f' {cell} |'

        return buffer


if __name__ == '__main__':

    cell_list = list()
    for v in range(1, 10):
        cell_list.append(Cell(v))

    line = Line(cell_list)
    print(line)

    cell_list = list()
    for v in range(2, 10):
        cell_list.append(Cell(0))

    cell_list.append(Cell(1))
    line = Line(cell_list)
    print(cell_list[0].possible_value)

    line.find_only_value()
    print(cell_list[0].possible_value)

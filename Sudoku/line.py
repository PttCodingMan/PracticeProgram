from cell import Cell
import util


class Line:
    def __init__(self, cell_list: list):
        util.check_value_count('Line', cell_list)

        self.cell_list = cell_list

    def find_only_value(self, map):
        for i_0, cell_0 in enumerate(self.cell_list):
            for i_1, cell_1 in enumerate(self.cell_list):
                if i_0 == i_1:
                    continue
                remove_result = cell_1.remove_possible_value(map, cell_0.value)
                if remove_result == Cell.CONTRADICT:
                    return Cell.CONTRADICT
        return Cell.OK

    def remove_possible_value(self, map, value):
        for cell in self.cell_list:
            remove_result = cell.remove_possible_value(map, value)
            if remove_result == Cell.CONTRADICT:
                return Cell.CONTRADICT

    def set_value(self, map, pos, value):
        result = Cell.OK
        for i, cell in enumerate(self.cell_list):
            if i == pos:
                continue
            find_result = cell.remove_possible_value(map, value)
            if find_result == Cell.CONTRADICT:
                return find_result

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

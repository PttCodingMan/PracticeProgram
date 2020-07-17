from cell import Cell
import util


class Line:
    def __init__(self, cell_list: list):
        util.check_value_count('Line', cell_list)

        self.possible_value = [x for x in range(1, 10)]
        for cell in cell_list:
            if cell.value not in self.possible_value:
                continue
            self.possible_value.remove(cell.value)
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

    def find_only_value(self):
        result = list()
        value_list = [0] * 10
        for cell in self.cell_list:
            if cell.value != 0:
                continue
            for possible_value in cell.possible_value:
                value_list[possible_value] += 1

        if 1 not in value_list:
            return result
        for i, count in enumerate(value_list):
            if count == 1:
                for cell in self.cell_list:
                    if i in cell.possible_value:
                        result.append((cell, i))
                        break
                break
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

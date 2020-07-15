from cell import Cell
import util


class Jiugongge:
    def __init__(self, cell_list: list):

        util.check_value_count('Jiugongge', cell_list)

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

    def set_value(self, pos, value):
        result = Cell.NOT_FIND
        for i, cell in enumerate(self.cell_list):
            if i == pos:
                continue
            find_result = cell.remove_possible_value(value)
            if find_result == Cell.CONTRADICT:
                return find_result
            if find_result == Cell.FIND:
                result = find_result
        return result

from cell import Cell
import util


class Jiugongge:
    def __init__(self, cell_list: list):

        util.check_value_count('Jiugongge', cell_list)

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

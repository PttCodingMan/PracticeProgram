from cell import Cell
import util


class Jiugongge:
    def __init__(self, cell_list: list):

        util.check_value_count('Jiugongge', cell_list)

        self.cell_list = cell_list

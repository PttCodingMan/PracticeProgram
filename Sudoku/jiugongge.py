from cell import Cell


class Jiugongge:
    def __init__(self, cell_list: list):

        if len(cell_list) != 9:
            raise ValueError('cell list length must be 9')

        self.cell_list = cell_list



import copy

from cell import Cell
from line import Line
from jiugongge import Jiugongge


class Sudoku:

    def __init__(self, value: str = None, obj=None):
        if value is not None:
            value = value.strip()
            value = value.replace('\n', '')
            if len(value) != 81:
                print(len(value))
                raise ValueError('Input length must be 81')

            self.cell_map = list()
            self.row_line = list()

            for i, v in enumerate(value):
                y = int(i / 9)
                x = i % 9
                if x == 0:
                    temp_list = list()
                current_cell = Cell(int(v))

                temp_list.append(current_cell)

                if x == 8:
                    self.cell_map.append(temp_list)
                    current_list = Line(temp_list)
                    self.row_line.append(current_list)

            self.column_line = list()

            for i in range(9):
                temp_list = list()
                for line in self.row_line:
                    temp_list.append(line.cell_list[i])
                    # print(line.cell_list[i])
                current_list = Line(temp_list)
                self.column_line.append(current_list)

            self.jiugongge_list = list()
            for y in range(0, 9, 3):
                for x in range(0, 9, 3):
                    # print('=' * 20)
                    # print(y, x)

                    current_list = list()

                    current_list.append(self.cell_map[y][x + 0])
                    current_list.append(self.cell_map[y][x + 1])
                    current_list.append(self.cell_map[y][x + 2])

                    current_list.append(self.cell_map[y + 1][x + 0])
                    current_list.append(self.cell_map[y + 1][x + 1])
                    current_list.append(self.cell_map[y + 1][x + 2])

                    current_list.append(self.cell_map[y + 2][x + 0])
                    current_list.append(self.cell_map[y + 2][x + 1])
                    current_list.append(self.cell_map[y + 2][x + 2])

                    current_jiugongge = Jiugongge(current_list)

                    self.jiugongge_list.append(current_jiugongge)
        # else:
        #     self.cell_map = copy.deepcopy(obj.cell_map)
        #     self.row_line = copy.deepcopy(obj.row_line)
        #     self.column_line = copy.deepcopy(obj.column_line)
        #     self.jiugongge_list = copy.deepcopy(obj.jiugongge_list)

    def find_only_answer(self):
        pass



    def __str__(self):
        buffer = '|' + '---|' * 9 + '\n'
        for i, line in enumerate(self.row_line):
            buffer += str(line) + '\n'
            buffer += '|'
            if i % 3 == 2:
                buffer += '---|' * 9 + '\n'
            else:
                buffer += ' - |' * 9 + '\n'
        return buffer


if __name__ == '__main__':
    value = '''
000015600
000060850
000000003
208000004
040390002
601200000
480670000
000800090
006040000
'''
    map = Sudoku(value=value)
    print(map)

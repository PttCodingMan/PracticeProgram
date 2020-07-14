from cell import Cell
from line import Line


class Sudoku:

    def __init__(self, value: str):
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

        for y in range(0, 9, 3):
            for x in range(0, 9, 3):
                print('=' * 20)
                print(y, x)



                # 0, 3, 6
        #
        #
        # print(self.cell_map[0][4].value)

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
    map = Sudoku(value)
    print(map)

import sys
import copy
import json

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
            self.empty_cell = 81

            for i, v in enumerate(value):
                y = int(i / 9)
                x = i % 9
                if x == 0:
                    temp_list = list()
                current_cell = Cell(self, y, x, int(v))

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

            self.contradicted = False
        # else:
        #     self.cell_map = json.loads(json.dumps(obj.cell_map))

    def check(self):

        map = copy.deepcopy(self)
        map.find_only_answer()
        return not map.contradicted

    def count_possible_value(self):
        result = Cell.OK
        for y in range(9):
            for x in range(9):
                cell = self.cell_map[y][x]
                if cell.value == 0:
                    continue
                remove_result = self.remove_possible_value(cell)
                if remove_result == Cell.CONTRADICT:
                    self.contradicted = True
                    return
                if remove_result == Cell.FIND:
                    result = Cell.FIND
        return result

    def find_only_answer(self):

        # 1. count cells possible values
        # 2. if number of possible value == 1
        #       set_value
        #       remove value from the possible value of other cell

        find = True
        while find:
            find = False
            for y in range(9):
                for x in range(9):
                    cell = self.cell_map[y][x]
                    if cell.value != 0:
                        continue
                    if len(self.cell_map[y][x].possible_value) == 1:
                        find = True
                        cell.set_value(self, self.cell_map[y][x].possible_value[0])

                        result = self.remove_possible_value(cell)
                        if result == Cell.CONTRADICT:
                            self.contradicted = True
                            return
                    if self.finish():
                        return

    def remove_possible_value(self, cell):

        # remove possible value from the relative cell

        y = cell.y
        x = cell.x

        result = Cell.OK

        remove_result = self.row_line[y].remove_possible_value(cell.value)
        if remove_result == Cell.CONTRADICT:
            return Cell.CONTRADICT
        if remove_result == Cell.FIND:
            result = Cell.FIND
        remove_result = self.column_line[x].remove_possible_value(cell.value)
        if remove_result == Cell.CONTRADICT:
            return Cell.CONTRADICT
        if remove_result == Cell.FIND:
            result = Cell.FIND

        index = int(y / 3) * 3 + int(x / 3)
        remove_result = self.jiugongge_list[index].remove_possible_value(cell.value)
        if remove_result == Cell.CONTRADICT:
            return Cell.CONTRADICT
        if remove_result == Cell.FIND:
            result = Cell.FIND

        return result

    def search(self):
        if self.finish():
            return
        self.count_possible_value()
        self.find_only_answer()
        if self.finish():
            return
        answer_map = self.recursive_search()
        if answer_map is None:
            return

        self.cell_map = answer_map.cell_map
        self.row_line = answer_map.row_line
        self.column_line = answer_map.column_line
        self.jiugongge_list = answer_map.jiugongge_list

    def recursive_search(self):
        min_degree = 10
        min_cell = None

        for cell_list in self.cell_map:
            for cell in cell_list:
                if cell.value != 0:
                    continue
                if len(cell.possible_value) < min_degree:
                    min_degree = len(cell.possible_value)
                    min_cell = cell

        for possible_value in min_cell.possible_value:
            map = copy.deepcopy(self)

            cell = map.cell_map[min_cell.y][min_cell.x]
            cell.set_value(map, possible_value)
            result = map.remove_possible_value(cell)
            if result == Cell.CONTRADICT:
                continue

            map.find_only_answer()
            if map.contradicted:
                continue

            if map.finish():
                return map
            map = map.recursive_search()
            if map is None:
                continue

            return map

        return None

    def finish(self):
        return self.empty_cell == 0

    def __str__(self):
        buffer = '    0   1   2   3   4   5   6   7   8' + '\n'
        buffer += '  |' + '---|' * 9 + '\n'

        for i, line in enumerate(self.row_line):
            buffer += f'{i} ' + str(line) + '\n'
            buffer += '  |'
            if i % 3 == 2:
                buffer += '---|' * 9 + '\n'
            else:
                buffer += ' - |' * 9 + '\n'
        for y in range(9):
            line = ''
            for x in range(9):
                line = f'{line}{self.cell_map[y][x].value}'
            buffer = f'{buffer}\n{line}'
        return buffer


if __name__ == '__main__':

    import time

    value_1 = '''
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
    value_2 = '''
534678912
672195348
198342567
859761423
426053791
713924856
961537284
287419635
345286170
'''
    value_2 = value_2.replace('2', '0')
    value = '0' * 81

    value_3 = '''
530070000
600195000
098000060
800060003
400803001
700020006
060000280
000419005
000080079    
'''
    hardest = '''800000000003600000070090200050007000000045700000100030001000068008500010090000400'''

    map = Sudoku(value=hardest)
    print(map)

    if not map.check():
        print('No answer')
        sys.exit()

    start_time = time.time()
    map.search()
    end_time = time.time()
    print(map)
    total_time = end_time - start_time
    print(f'共耗費時間 %.2f 秒' % total_time)

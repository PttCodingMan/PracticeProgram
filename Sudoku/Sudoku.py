import sys
import copy

from cell import Cell
from line import Line
from jiugongge import Jiugongge


class Sudoku:
    def __init__(self, value: str):
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

    def check(self):

        map = copy.deepcopy(self)
        map.find_only_answer()
        return not map.contradicted

    def find_only_answer(self):

        if self.finish():
            return

        for line in self.row_line:
            find_result = line.find_only_value(self)
            if find_result == Cell.CONTRADICT:
                self.contradicted = True
                return

        for line in self.column_line:
            find_result = line.find_only_value(self)
            if find_result == Cell.CONTRADICT:
                self.contradicted = True
                return

        for jiugongge in self.jiugongge_list:
            find_result = jiugongge.find_only_value(self)
            if find_result == Cell.CONTRADICT:
                self.contradicted = True
                return

    def remove_possible_value(self, cell):
        y = cell.y
        x = cell.x

        self.row_line[y].remove_possible_value(self, cell.value)
        self.column_line[x].remove_possible_value(self, cell.value)

        index = int(y / 3) * 3 + int(x / 3)

        self.jiugongge_list[index].remove_possible_value(self, cell.value)
        self.find_only_answer()

    def set_value(self, y, x, value):
        result = Cell.NOT_FIND
        set_result = self.row_line[y].set_value(x, value)
        if set_result == Cell.CONTRADICT:
            return set_result
        if set_result == Cell.FIND:
            result = set_result

        set_result = self.column_line[x].set_value(y, value)
        if set_result == Cell.CONTRADICT:
            return set_result
        if set_result == Cell.FIND:
            result = set_result

        index = int(y / 3) * 3 + int(x / 3)
        # print(f'{y} {x} = {index}')

        pos_y = int(y % 3)
        pos_x = int(x % 3)
        pos = pos_y * 3 + pos_x

        set_result = self.jiugongge_list[index].set_value(pos, value)
        if set_result == Cell.CONTRADICT:
            return set_result
        if set_result == Cell.FIND:
            result = set_result

        self.cell_map[y][x].set_value(value)

        return result

    def search(self):

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
        print('================')
        min_degree = 10
        min_cell = None

        for cell_list in self.cell_map:
            for cell in cell_list:
                if cell.value != 0:
                    continue
                if len(cell.possible_value) < min_degree:
                    min_degree = len(cell.possible_value)
                    min_cell = cell

        # print(min_degree)
        # print(min_cell.y, min_cell.x)
        # print(min_cell.possible_value)

        for possible_value in min_cell.possible_value:
            # print(possible_value)
            map = copy.deepcopy(self)
            # print(map.cell_map[4][0].possible_value)
            # print(map.cell_map[4][2].possible_value)
            # map.cell_map[min_cell.y][min_cell.x].set_value(possible_value)
            set_result = map.set_value(min_cell.y, min_cell.x, possible_value)
            if set_result == Cell.CONTRADICT:
                continue
            if set_result == Cell.FIND:
                map.find_only_answer()
            # if map.contradicted:
            #     # print('contradicted')
            #     continue
            if self.answer is not None:
                return
            if map.finish():
                # self.answer = copy.deepcopy(map)
                return map

            # print(map)
            # print(map.cell_map[4][0].possible_value)
            # print(map.cell_map[4][2].possible_value)
            break
            # map = map.recursive_search()
            # if map is None:
            #     continue
            # if map.finish():
            #     # self.answer = copy.deepcopy(map)
            #     return map

        return None

    def finish(self):
        if self.empty_cell == 0:
            return True
        return False

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
        return buffer


if __name__ == '__main__':

    # for y in range(9):
    #     for x in range(9):
    #
    #
    #         pos_y = int(y % 3)
    #         pos_x = int(x % 3)
    #         print(pos_y, pos_x, pos_y * 3 + pos_x)
    #
    #         index = y + int(x / 3)
    #         print(f'{y} {x} = {index}')
    #         print('=====')
    #
    # sys.exit()

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
    # value = '0' * 81
    map = Sudoku(value=value_2)
    print(map)

    if not map.check():
        print('No answer')
        sys.exit()
    map.search()
    print(map)

    # for y in range(9):
    #     for x in range(9):
    #         if map.cell_map[y][x].value != 0:
    #             continue
    #         print(map.cell_map[y][x].possible_value)


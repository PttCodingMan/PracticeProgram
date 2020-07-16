import os
import sys
import time


class f:
    def __init__(self, n):
        self.map = [[-1 for x in range(n)] for i in range(n)]
        self.star = [['*' for x in range(n)] for i in range(n)]
        self.total = 0
        self.end = n

    def count(self, lv):
        if lv == self.end:
            return
        for i in range(self.end):
            # find a point empty
            if self.map[lv][i] == -1:
                # take this point
                self.map[lv][i] = lv
                if lv != self.end - 1:
                    # 展開限制條件
                    self.walk(lv, i, lv)
                self.star[lv][i] = 'Q'
                # recursive next
                self.count(lv + 1)
                if lv == self.end - 1:
                    self.show()
                    self.total = self.total + 1
                if lv != self.end - 1:
                    # 還原限制條件
                    self.walk(lv, i, -1)

                self.map[lv][i] = -1
                self.star[lv][i] = '*'
        return

    def walk(self, x, y, ch):
        for i in range(self.end):
            if i != x and (self.map[i][y] == -1 or self.map[i][y] == self.map[x][y]):
                self.map[i][y] = ch
            if (not (x + i >= self.end or y + i >= self.end)) and (not i == 0) and (
                    self.map[x + i][y + i] == -1 or self.map[x + i][y + i] == self.map[x][y]):
                self.map[x + i][y + i] = ch
            if x + i < self.end and i != 0 and y - i >= 0 and (
                    self.map[x + i][y - i] == -1 or self.map[x + i][y - i] == self.map[x][y]):
                self.map[x + i][y - i] = ch

    def show(self):
        # return
        for i in range(self.end):
            buff = ''
            for x in range(self.end):
                # print self.star[i][x],
                if len(buff) == 0:
                    buff = self.star[i][x]
                else:
                    buff += ' ' + self.star[i][x]
            print(buff)
        print('')


print(sys.argv)
if len(sys.argv) == 2:
    how = int(sys.argv[1])
else:
    how = int(
        input(' ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  == \nHow many Q:'))
print('')
x = f(how)
StartTime = time.time()
x.count(0)
EndTime = time.time()
print(how, '階方陣總共為', x.total, '種解答')
print(f'共耗時 {round(EndTime - StartTime, 1)} 秒')

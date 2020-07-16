import sys
import time

from sudoku import Sudoku

topic = '''
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

map = Sudoku(topic)
print(map)

if not map.check():
    print('No answer')
    sys.exit()

start_time = time.time()
map.search()
end_time = time.time()
print(map)
total_time = end_time - start_time
print(f'Time %.2f s' % total_time)

# also, topic can be a int list
topic = [
    8, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 3, 6, 0, 0, 0, 0, 0,
    0, 7, 0, 0, 9, 0, 2, 0, 0,
    0, 5, 0, 0, 0, 7, 0, 0, 0,
    0, 0, 0, 0, 4, 5, 7, 0, 0,
    0, 0, 0, 1, 0, 0, 0, 3, 0,
    0, 0, 1, 0, 0, 0, 0, 6, 8,
    0, 0, 8, 5, 0, 0, 0, 1, 0,
    0, 9, 0, 0, 0, 0, 4, 0, 0]

map = Sudoku(topic)
print(map)


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
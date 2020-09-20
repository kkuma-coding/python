from microbit import *

pos = 0
SIZE = 5
MAX = 25

def draw(pos):
    x = int(pos % SIZE)
    y = int (pos / SIZE)
    display.set_pixel (x, y, int(pos % SIZE)+1)
    '''
    0 % 5 == 0
    1 % 5 == 1
    2 % 5 == 2
    3 % 5 == 5
    ..
    ..
    24
    '''

while True:
    for position in range (0, MAX):
        draw(position)
        sleep(100)
    sleep(1000)
    display.clear()
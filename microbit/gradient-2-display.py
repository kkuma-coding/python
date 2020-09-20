from microbit import *

pos = 0
SIZE = 5
MAX = 25

def draw(pos):
    x = int(pos % SIZE)
    y = int (pos / SIZE)
    display.set_pixel (x, y, int(pos % SIZE)+1)

for position in range (0, 25):
    draw(position)
    sleep(100)

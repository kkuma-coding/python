from microbit import *

'''
map = [[1, Image.CLOCK1],
       [2, Image.CLOCK2],
       [3, Image.CLOCK3],
       [4, Image.CLOCK4],
       [5, Image.CLOCK5],
       [6, Image.CLOCK6],
       [7, Image.CLOCK7],
       [8, Image.CLOCK8],
       [9, Image.CLOCK9],
       [10, Image.CLOCK10],
       [11, Image.CLOCK11],
       [12, Image.CLOCK12]]

print (map[0][1])
'''

while True:
    for hour in range (1, 12):
        if hour == 1:
            display.show(Image.CLOCK1)
        elif hour == 2:
            display.show(Image.CLOCK2)
        elif hour == 3:
            display.show(Image.CLOCK3)
        elif hour == 4:
            display.show(Image.CLOCK4)
        elif hour == 5:
            display.show(Image.CLOCK5)
        elif hour == 6:
            display.show(Image.CLOCK6)
        elif hour == 7:
            display.show(Image.CLOCK7)
        elif hour == 8:
            display.show(Image.CLOCK8)
        elif hour == 9:
            display.show(Image.CLOCK9)
        elif hour == 10:
            display.show(Image.CLOCK10)
        elif hour == 11:
            display.show(Image.CLOCK11)
        elif hour == 12:
            display.show(Image.CLOCK12)
        sleep(100)

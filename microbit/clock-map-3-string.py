from microbit import *

map = [[1, "Image.CLOCK1", Image.CLOCK1],
       [2, "Image.CLOCK2"],
       [3, "Image.CLOCK3"],
       [4, "Image.CLOCK4"],
       [5, "Image.CLOCK5"],
       [6, "Image.CLOCK6"],
       [7, "Image.CLOCK7"],
       [8, "Image.CLOCK8"],
       [9, "Image.CLOCK9"],
       [10, "Image.CLOCK10"],
       [11, "Image.CLOCK11"],
       [12, "Image.CLOCK12"]]


while True:
    # display.scroll((map[0][1]))
    display.show((map[0][2]))

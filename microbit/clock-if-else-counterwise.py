from microbit import *

while True:
    for hour in range (1, 12):
        if hour == 1:
            display.show(Image.CLOCK12)
        elif hour == 2:
            display.show(Image.CLOCK11)
        elif hour == 3:
            display.show(Image.CLOCK10)
        elif hour == 4:
            display.show(Image.CLOCK9)
        elif hour == 5:
            display.show(Image.CLOCK8)
        elif hour == 6:
            display.show(Image.CLOCK7)
        elif hour == 7:
            display.show(Image.CLOCK6)
        elif hour == 8:
            display.show(Image.CLOCK5)
        elif hour == 9:
            display.show(Image.CLOCK4)
        elif hour == 10:
            display.show(Image.CLOCK3)
        elif hour == 11:
            display.show(Image.CLOCK2)
        elif hour == 12:
            display.show(Image.CLOCK1)
        sleep(100)

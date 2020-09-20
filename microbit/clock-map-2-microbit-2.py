map = [[1,  "Image.CLOCK1"],
       [2,  "Image.CLOCK2"],
       [3,  "Image.CLOCK3"],
       [4,  "Image.CLOCK4"],
       [5,  "Image.CLOCK5"],
       [6,  "Image.CLOCK6"],
       [7,  "Image.CLOCK7"],
       [8,  "Image.CLOCK8"],
       [9,  "Image.CLOCK9"],
       [10, "Image.CLOCK10"],
       [11, "Image.CLOCK11"],
       [12, "Image.CLOCK12"]]

for hour in range (0, 12):
       print ("{}\t{}".format(hour, map[hour][1]))

'''
print ("position {}, {}".format(  map[0][2], map[0][3]))
print ("position {0}, {1}".format(map[0][2], map[0][3]))
print ("position {1}, {0}".format(map[0][2], map[0][3]))
'''
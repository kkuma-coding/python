# https://hourofpython.trinket.io/python-challenges#/string-challenges/oxford-comma-challenge

# Make a function commafy that, given a list of three or more things,
# returns a list with commas.
#
# >>>> commafy(["trinket", "learning", "fun"])
# trinket, learning, and fun
# >>>> commafy(["lions", "tigers", "bears"])
# lions, tigers, and bears

def commafy(list):
    # Add code here that returns the answer
    # "{}, {}, and {}".format(list[0], list[1], list[2])
    string = ""
    for word in list[:-1:]:
        string += word
        string += ", "
    string += "and "
    string += list[-1::][0]
    return string

# Add print statements here to test what your code does:
print (commafy(["trinket", "learning", "fun"]))

print (commafy(["lions", "tigers", "bears"]))
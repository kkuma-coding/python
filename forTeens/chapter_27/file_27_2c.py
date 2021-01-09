#Define the function 
def display(color, exists):
    neg = ""
    if exists == False:
        neg = "n't any"

    return "There is" + neg + " " + color + " in the rainbow"

#Main code starts here
print(display("red", True))
print(display("yellow", True))
print(display("black", False))

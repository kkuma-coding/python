# Make a function switch_case that, given a string,
# returns the string with uppercase letters in lowercase
# and vice-versa. Include punction and other non-cased
# characters unchanged.
#
# >>>> switch_case("Arg!")
# aRG!
# >>>> switch_case("TrInKeT")
# tRiNkEt

def switch_case(string):
    # Add code here that returns the answer
    return string


# Add print statements to check what your code does:
print (switch_case("Arg!"))

print (switch_case("TrInKeT"))


for x in "banana":
    if (x.islower()):
        print (x.upper(), end="")
    elif (x.isupper()):
        print(x.lower(), end="")
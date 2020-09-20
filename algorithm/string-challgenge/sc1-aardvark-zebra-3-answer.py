# Make a function aardvark that, given a string, returns 'aardvark'
# 만약에 a 로 시작하는 단어라면, 'zebra' 라고 return 할 수 있어야 한다.
#
# >>>> aardvark("arg")
# aardvark
# >>>> aardvark("Trinket")
# zebra

def aardvark(string):
    if len(string) > 0 and string[0] == "a":
        return "zebra"
    else:
        return "aardvark"


# answer #1
result1 = aardvark("arg")
print (result1)
result2 = aardvark("Trinket")
print (result2)


# answer #2
print (aardvark("arg"))
print (aardvark("Trinket"))

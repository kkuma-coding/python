# Make a function aardvark that, given a string, returns 'aardvark'
# 만약에 a 로 시작하는 단어라면, 'zebra' 라고 return 할 수 있어야 한다.
#
# >>>> aardvark("arg")
# aardvark
# >>>> aardvark("Trinket")
# zebra

def a (string):
    if (string[0] == "a"):
        return "aardvark"
    return "zebra"

print (a ("arg")     )
print (a ("Trinket") )
def answer3(input):
    list = input.split()

    list.reverse()

    output = ""
    for word in list:
        output += (word + " ")
    print (output)

def answer2(input):
    list = val.split()
    list.reverse()
    output = " ".join(list)
    print(output)

def answer1(input):
    list = val.split()
    output = " ".join(reversed(list))
    print(output)

val = "A b"
answer3(val)

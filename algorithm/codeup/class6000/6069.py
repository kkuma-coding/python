'''
https://codeup.kr/problem.php?id=6069
A : best!!!
B : good!!
C : run!
D : slowly~
'''

my_map = {
    "A" : "best!!!",
    "B" : "good!!",
    "C" : "run!",
    "D" : "slowly~"
}
key = input()
if (my_map.__contains__(key)):
    print(my_map[key])
else:
    print("what?")
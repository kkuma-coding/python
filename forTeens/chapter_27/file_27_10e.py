def display_values():
    x = 7
    y = 3
    print(x, y)     #It displays: 7  3

def display_other_values():
    y = 2
    print(x, y)     #It displays: 10  2

#Main code starts here
x = 10              #x is global            
print(x)            #It displays: 10
display_values()
display_other_values()
print(x)            #It displays: 10

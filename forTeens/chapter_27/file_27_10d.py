def display_value():
    global test
    print(test)    #It displays: 10
    test = 20
    print(test)    #It displays: 20

#Main code starts here
test = 10
display_value()
print(test)        #It displays: 20

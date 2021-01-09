#Define the function divide(). 
#The arguments n1 and n2 are called formal arguments
def divide(n1, n2):
    result = n1 / n2
    return result

#Main code starts here
x = float(input())
y = float(input())

#Call the function divide(). 
#The arguments x and y are called actual arguments
w = divide(x, y)

print(w)

text = "I have a dream"

letter = input("Enter a letter to search: ")

found = False
for x in text:
    if x == letter:
        found = True
        break

if found == True:
    print("Letter", letter, "found!")

def prepend_title(first_name, last_name, title = "Mr", reverse = False):
    if reverse == False:
        return title + " " + first_name + " " + last_name
    else:
        return title + " " + last_name + " " + first_name

#Main code starts here
print(prepend_title("John", "King"))               #It displays: Mr John King
print(prepend_title("Maria", "Myles", "Ms"))       #It displays: Ms Maria Myles
print(prepend_title("Maria", "Myles", "Ms", True)) #It displays: Ms Miller Myles

#Using keyword argument
print(prepend_title("John", "King", reverse = True)) #it displays: Mr King John

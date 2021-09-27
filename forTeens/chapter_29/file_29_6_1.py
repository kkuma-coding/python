class Romans:

    def __init__(self):
        self._number = None   #Private field. It does not call the setter!

    #Define the getter
    @property
    def number(self):
        return self._number

    #Define the setter
    @number.setter
    def number(self, value):
        if value >=1 and value <= 5: 
            self._number = value
        else:
            raise ValueError("Number not recognized")    

    #Define the getter
    @property
    def roman(self):
        number2roman = {1:"I", 2:"II", 3:"III", 4:"IV", 5:"V"}
        return number2roman[self._number]

    #Define the setter
    @roman.setter
    def roman(self, value):
        roman2number = {"I":1, "II":2, "III":3, "IV":4, "V":5}
        if value in roman2number:
            self._number = roman2number[value]
        else:
            raise ValueError("Roman numeral not recognized")    

#Main code starts here
x = Romans()

x.number = 3
print(x.number)     #It displays: 3
print(x.roman)      #It displays: III

x.roman = "V"
print(x.number)     #It displays: 5
print(x.roman)      #It displays: V

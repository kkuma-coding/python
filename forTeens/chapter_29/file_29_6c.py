class FahrenheitToCelsius:
    def __init__(self, value):
        self.set_temperature(value)

    def get_temperature(self):
        return 5.0 / 9 * (self._temperature - 32)

    def set_temperature(self, value):
        if value >= -459.67: 
            self._temperature = value
        else:
            raise ValueError("There is no temperature below -459.67")    

    #Define a property
    temperature = property(get_temperature, set_temperature)

#Main code starts here
x = FahrenheitToCelsius(-50)

print(x.temperature)        #This calls the method get_temperature()

x.temperature = -500        #This calls the method set_temperature()
                            #and throws an error

print(x.temperature)        #This calls the method get_temperature()

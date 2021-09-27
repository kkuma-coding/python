class FahrenheitToCelsius:
    def __init__(self, value):
        self.set_temperature(value)

    def get_temperature(self):
        return 5.0 / 9.0 * (self.temperature - 32.0)

    def set_temperature(self, value):
        if value >= -459.67: 
            self.temperature = value
        else:
            raise ValueError("There is no temperature below -459.67")

#Main code starts here
x = FahrenheitToCelsius(-50)
print(x.get_temperature())

class FahrenheitToCelsius:
    def __init__(self, value):
        self.temperature = value

    def get_temperature(self):
        return 5.0 / 9.0 * (self.temperature - 32.0)

#Main code starts here
x = FahrenheitToCelsius(-68)
print(x.get_temperature())

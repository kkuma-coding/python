
class Greeter (object):
    # constructor
    def __init__(self, name):
        self.name = name # Create an instance variable

    def greet(self, loud=False):
        if loud:
            print ('HELLO, %s' % self.name.upper())
        else:
            print ('Hello, %s' % self.name)

g = Greeter('john')
g.greet()
g.greet(loud=True)
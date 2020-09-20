
class Person (object):
    # constructor
    def __init__(self, name):
        self.name = name # Create an instance variable
        self.age = None

    def introduce(self, loud=False):
        if loud:
            print ('HELLO, my name is %s' % self.name.upper())
        else:
            print ('Hello, my name is %s' % self.name)

    def set_age(self, age):
        pass

g = Person('john')
g.introduce()
g.introduce(loud=True)
from human import Human

class Adult(Human):
    def __init__(self, name):
        self.name = name
        self.self_introduce_message = "I'm adult"

    def get_introduce_message(self):
        return self.self_introduce_message

'''
class Adult(Human):
    pass

a = Adult("dad")
print(a.get_name())
print(a.get_introduce_message())
'''
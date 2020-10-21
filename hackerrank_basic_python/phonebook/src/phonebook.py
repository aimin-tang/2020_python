class PhoneBook:
    def __init__(self):
        self.dict = {}

    def add(self, name, number):
        self.dict[name] = number

    def lookup(self, name):
        return self.dict[name]

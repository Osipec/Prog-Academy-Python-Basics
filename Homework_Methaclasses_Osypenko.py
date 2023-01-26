class MetaSaver(type):
    def __new__(typeclass, classname, supers, classdict):
        return type.__new__(typeclass, classname, supers, classdict)
    def __init__(cls, classname, supers, classdict):
        with open('class_info.txt', 'w') as file:
            file.write(f'{classname}; {[item for item in classdict]}\n')

class Cat(metaclass=MetaSaver):
    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour

    def __str__(self):
        return f'{self.name}, {self.age}, {self.colour}'

    def test(self):
        ...

my_cat = Cat('Eva', 8, 'Black')


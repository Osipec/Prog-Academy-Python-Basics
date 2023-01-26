import datetime


# 1. Create descriptor that makes read-only attributes
#
class MyDescriptor:
    def __init__(self, atribute):
        self.atribute = atribute

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.atribute)

    def __set__(self, instance, value):
        if self.atribute not in instance.__dict__:
            instance.__dict__[self.atribute] = value
        else:
            raise AttributeError()

    def __del__(self):
        return AttributeError()


class Cat:
    def __init__(self, name, age, colour, owner='Petro'):
        self.name = name
        self.age = age
        self.colour = colour
        self.owner = owner

    def __str__(self):
        return '; '.join(map(lambda item: f'[{item[0]}]: {item[1]}', self.__dict__.items()))

    owner = MyDescriptor('owner')


my_cat = Cat('Sana', 5, 'Ginger')
print(my_cat)
my_cat.owner = 'Ivan'


# 2, 3. Only integer attribute. Write attribute value to a file

class Dog:
    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour

    @property
    def age(self):
        return {self.__age}

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError()
        with open('age.txt', 'a') as file:
            file.write(f'New age = {value}; {datetime.datetime.now()}\n')
        self.__age = value

    @age.deleter
    def age(self):
        ...

    def __str__(self):
        return '; '.join(map(lambda item: f'[{item[0]}]: {item[1]}', self.__dict__.items()))


my_dog = Dog('Palkan', 12, 'Black')
print(my_dog)
my_dog.age = 22
print(my_dog)

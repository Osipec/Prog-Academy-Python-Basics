from abc import ABC, abstractmethod
import sympy


class BaseSimpleClass(ABC):
    @abstractmethod
    def is_simple(self):
        ...


class SimpleFromBase(BaseSimpleClass):
    def __init__(self, number):
        self.number = number

    def is_simple(self):
        if sympy.isprime(self.number):
            return True
        return False


class SimpleNums:
    def __init__(self, number):
        self.number = number

    def is_simple(self):
        if sympy.isprime(self.number):
            return True
        return False


number_1 = SimpleFromBase(7)
print(number_1.is_simple())
print(isinstance(number_1, BaseSimpleClass))

number_2 = SimpleNums(6)
print(number_2.is_simple())
print(isinstance(number_2, BaseSimpleClass))

BaseSimpleClass.register(SimpleNums)
print(isinstance(number_2, BaseSimpleClass))

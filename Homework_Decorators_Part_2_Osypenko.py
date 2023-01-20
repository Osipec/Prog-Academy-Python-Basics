# Homework. Decorators_part_2. Osypenko Kostiantyn

# 1. Create a decorator that registers classes in list

class ClassRegistrator:
    """
    This is a class-decorator which adds a decorated class in to a list of called classes
    """
    class_list = []

    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        if self.cls not in self.class_list:
            self.class_list.append(self.cls.__name__)
        return self.cls


@ClassRegistrator
class X:
    def __init__(self, x):
        self.x = x


@ClassRegistrator
class A:
    def __init__(self, a):
        self.a = a


x = X(2)
instance = A(2)
print(A.class_list)


# 2, 3. Create a class decoraor which adds a string to a class __str__.
#       Create a static method to count volume of two boxes

class StrDecorator:
    """
    This decorator adds a specific text to the left of the result of __str__ method of decorated class.
    Specific text is an atribute of decirator
    """

    def __init__(self, text):
        self.text = text

    def __call__(self, func):
        def inner(*args, **kwargs):
            data = self.text + func(*args, **kwargs)
            return data

        return inner


class Box:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @StrDecorator('Hello ')
    def __str__(self):
        return f'Box A: {self.a}, B: {self.b}, C: {self.c}'

    def volume(self):
        return self.a * self.b * self.c

    @staticmethod
    def volume_of_two(box_1, box_2):
        return f'Total volume of boxes is {box_1.volume() + box_2.volume()}'


box_1 = Box(1, 2, 3)
box_2 = Box(3, 4, 5)

print(box_1)
print(box_2)
print(Box.volume_of_two(box_1, box_2))

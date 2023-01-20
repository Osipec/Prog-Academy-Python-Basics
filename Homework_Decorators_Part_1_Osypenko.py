# Homework. Decorators_part_1. Osypenko Kostiantyn

# 1,2. Create decorators to count how many times function was called and decorator to register function

def counter(func):
    """
    This decorator counts how many times the decorated function was called
    :param func:
    :return: String with name of called function and times of calls
    """
    dictionary = {}

    def inner(*args, **kwargs):
        dictionary[func] = dictionary.get(func, 0) + 1
        print(f'Function {func.__name__} was called {dictionary[func]} times')
        return func(*args, **kwargs)

    return inner


registerd_functions = []


def registrator(func):
    """
    This decorator adds decorated function in to a list of called fuctions
    """
    registerd_functions.append(func.__name__)
    return func


@counter
@registrator
def summ(a, b):
    return a + b


@counter
@registrator
def mult(a, b):
    return a * b


@registrator
def div(a, b):
    return a // b


print(registerd_functions)

summ(5, 2)
summ(1, 1)
mult(2, 2)


# 3. Create decorator that saves __str__ method of class in a text file.

def string_saver(func):
    def inner_func(object, *args, **kwargs):
        with open(object.__class__.__name__, 'w') as file:
            file.write(func(object))
        return func(object)

    return inner_func


class Box:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @string_saver
    def __str__(self):
        return f'Box A: {self.a}, B: {self.b}, C: {self.c}'


box_1 = Box(1, 2, 3)
print(box_1)


# 4. Create a decorator to check function execution time

def time_logger(exec_num: int, file_name: str):
    """
    This decorator calculates execution time of functions.
    :param exec_num: Number of function executions to be made
    :param file_name: Name of file to write logging results
    :return: None
    """
    import datetime
    def decorator(func):
        def inner(*args, **kwargs):
            start_time = datetime.datetime.now()
            for i in range(exec_num):
                func(*args, **kwargs)
            end_time = datetime.datetime.now()
            exec_time = end_time - start_time
            with open(file_name, 'w') as file:
                file.write(f'Function "{func.__name__}" execution time {exec_time.total_seconds()}')
            return func(*args, **kwargs)

        return inner

    return decorator


@time_logger(2000, "cube")
def cube(num: int):
    num **= 100000
    return num


cube(10)

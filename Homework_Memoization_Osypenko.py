# Closures, Osypenko Kostiantyn

# 1. Create a gen function

def genertor(first_el: int | float, el_num: int, func):
    counter = 0
    while counter != el_num:
        yield func(first_el)
        counter += 1
        first_el += 1

def cubic_method(number):
    return number ** 3
def multy_method(number):
    return number * 2

seq = genertor(2, 6, cubic_method)
for i in seq:
    print(i)

# 2. Fibonacci + Memoization
from timeit import timeit

recursion = """
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))

for i in range(30):
    fibonacci(i)
"""

memoization = """
def memoize(func):
    cache = {}

    def decorate(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = func(*args)
            return cache[args]
    return decorate
    
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))

for i in range(30):
    fibonacci(i)
"""

print(f'Recursion time: {timeit(recursion, number=10)}')
print(f'Memoization time: {timeit(memoization, number=10)}')

# 3. Write a function to change a list of numbers

import random

def list_changer(list: list):
    new_list = []
    for item in list:
        if item % 2:
            new_list.append(1)
        else:
            new_list.append(item)
    return sum(new_list), new_list

user_list = [random.randint(1,20) for _ in range(10)]

print(list_changer(user_list))

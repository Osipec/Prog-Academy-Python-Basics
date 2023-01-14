# Generator functions and expressions. Osypenko Kostiantyn

# 1. Make generator function

def gen_func(number: int, n: int, limit: int):
    while number < limit:
        yield number
        number *= n


gen = gen_func(1, 2, 550)
for i in gen:
    print(i)


# 2. Create your own range function

def my_range(*args: int):
    for item in args:
        if not isinstance(item, int):
            raise ValueError()
    if len(args) == 1:
        start = 0
        stop = args[0]
        while start <= stop - 1:
            yield start
            start += 1
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
        if start > stop:
            return
        while start <= stop - 1:
            yield start
            start += 1
    elif len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
        if not step:
            raise ValueError('Step must not be equal to 0')
        if step > 0 and start > stop:
            return
        if step < 0 and start < stop:
            return
        if step < 0 and start > stop:
            while start > stop:
                yield start
                start += step
        while abs(start) <= abs(stop - 1):
            yield start
            start += step
    else:
        raise ValueError()

for i in my_range(50, 10, -5):
    print(i)

# 3. Simle number generator
def simple_gen(n):
    for number in range(2, n + 1):
        for i in range(2, number):
            if not number % i:
                break
        else:
            yield number

for i in simple_gen(100):
    print(i)

# 4. Genertor expression
gen = list(i**3 for i in range(2, 10))
print(gen)








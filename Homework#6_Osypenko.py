# Homework 6, Lesson 5, Osypenko Kostiantyn

# 1. All numbers from 1 to 100 %7:
for i in range(1, 101):
    if not i % 7:
        print(i)

# 2. Factorial
import math
number = int(input('Enter number: '))
fact = 1
for i in range(2, number + 1):
    fact *= i
print(f'Factorial of {number} is {fact}')
print(f'Factorial using math.factorial(number) is {math.factorial(number)}')

# 3. Multiply table
number = int(input('Enter number: '))
for i in range(1,11):
    print(f'{number} * {i} = {number * i}')

# 4. Print a square
columns = int(input('Enter number of columns: '))
raws = int(input('Enter number of rows: '))
for x in range(1, raws+1):
    if x == 1 or x == raws:
        print(f'{columns*"*"}')
    else:
        print(f'*{" "*(columns-2)}*')

# 5. [0,5,2,4,7,1,3,19], find Odds
given_list = [0, 5, 2, 4, 7, 1, 3, 19]
odds = [i for i in given_list if i % 2]
print(odds)

# 6. List of 4 random numbers plus doubled numbers
import random
base_list = [random.randint(1, 10) for i in range(4)]
print(base_list)
base_list += [i * 2 for i in base_list]
print(base_list)

# 7. Average salary
MONTHS = 12
year_salary = [12000, 13000, 10000, 15000, 10000, 14000, 15000, 7000, 11000, 16000, 9000, 15000]
print(f'{year_salary}\n{sum(year_salary)/MONTHS}')

# 8. Summ of matrix elements
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
summ = 0
for raw in matrix:
    print(*raw)
    summ+=sum(raw)
print(summ)

# 9. Reverse list
import random
lenght = int(input('Enter list lenght: '))
list = [random.randint(1, 10) for i in range(lenght)]
print(list)
list.reverse()
print(list)

# 10. All simple numbers from 1 to 100
def is_prime(number: int):
    if not number % 2 or number < 2:
        return False
    d = 3
    while d * d <= number and number % d != 0:
        d += 1
    return d * d > number

print(*[i for i in range(1, 101) if is_prime(i)])

# 11. Sandclock
while True:
    size = int(input("Enter clock size: "))
    if size % 2:
        break
    else:
        print('Clock size must be odd number')

stars = size
for i in range(size // 2):
    print(f'{" "*i}{"*"*stars}{" "*i}')
    stars-=2

print(f'{" "*(size//2)}{"*"*stars}{" "*(size//2)}')

counter = size//2 - 1
for i in range(size // 2):
    stars += 2
    print(f'{" " * counter}{"*" * stars}{" " * counter}')
    counter-=1

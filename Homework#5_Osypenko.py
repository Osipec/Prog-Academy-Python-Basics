# Lesson 4, Homework 5, Osypenko Kostiantyn

# 1.Check the number if it's lucky or not

def lucky_chekker(number: str) -> str:
    number1 = sum(int(i) for i in number[0:round(len(number) / 2)])
    number2 = sum(int(number[i]) for i in range(round(len(number) / 2), len(number)))
    return 'You\'ve got a lucky number!' if number1 == number2 else 'Your number is not lucky'

number = input('Enter the number to check if it\'s lucky\t')
if not len(number) % 2:
    print(lucky_chekker(number))
else:
    print('Your number must be multiples of two')

# 2. Palindrome

palindrome = input('Enter any number to check if it\'s palindrome\t')
print(palindrome == palindrome[::-1] and "Palindrome" or 'Not a palindrome')

# 3. Point in circle with given radius

import math

radius = int(input('Enter circle radius\t'))
coord_A, coord_B = int(input('Enter coordinate A\t')), int(input('Enter coordinate B\t'))
if math.hypot(coord_A, coord_B) > radius:
    print(f'Point ({coord_A},{coord_B}) not in circle with radius {radius}')
else:
    print(f'Point ({coord_A},{coord_B}) is in circle with radius {radius}')

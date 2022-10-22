import math

#Домашнее задание №1. Осипенко Костя. Для проверки уберите комментирование


# print('Hello world')

# print('My name\n','Is Kostya\n','I\'m 33\t')

def rect_area():
    lenght = int(input('Enter lenght:\t'))
    width = int(input('Enput width:\t'))
    area = lenght * width
    print(f'Area of rectangle is {area}')


# rect_area()

def two_numbers():
    number_one = int(input('Enter number one:\t'))
    number_two = int(input('Enput number two:\t'))
    print(f'Sum = {number_one + number_two}')
    print(f'Product = {number_one * number_two}')
    print(f'Difference = {number_one - number_two}')
    if number_two == 0:
        while not number_two:
            number_two = int(input(f'Number two is 0, you cand divide by it. Enter another value\t'))
        print(f'Quotient = {number_one / number_two}')
    else:
        print(f'Quotient = {number_one / number_two}')


# two_numbers()


def circle():
    radius = int(input('Enter the circle radius\t'))
    print(f'Circle diametr is {radius * 2}')
    print(f'Circle circumference is {2 * math.pi * radius}')
    print(f'Circle area is {math.pi * radius ** 2}')

#circle()

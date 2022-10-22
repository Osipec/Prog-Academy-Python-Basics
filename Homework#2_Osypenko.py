import math


# Домашнє завдання №2. Осипенко Костянтин. Для перевірки розкоментуйте потрібну частину

# 1. Construct an integer from the string "123"

# string = "123"
# integer = int(string)
# print(integer)

# 2. Construct a float from the integer 123

# integer = 123
# float_num = float(integer)
# print(float_num)

# 3. Construct an integer from the float 12.345
# float_num = 12.345
# int_num = int(float_num)
# print(int_num)

# 4. Write a Python-script that detects the last 4 digits of a credit card
def card_number():
    card_number = 1111111111112345
    last_4_digits = str(card_number)[-4:]
    print(last_4_digits)


card_number()


# 5. Write a Python-script that calculates the sum of the digits of a three-digit
#    number
def sum_of_digits():
    number = int(input('Enter 3-Digit number\t'))
    summ = 0
    counter = number
    while counter > 0:
        summ += counter % 10
        counter //= 10
    print(f'Sum of digits of number {number} is {summ}')


# sum_of_digits()


# 6. Write a program that calculates and displays the area of a triangle if its sides
#    are known
def triangle_area():
    side_a = int(input('Length of side A:\t'))
    side_b = int(input('Length of side B:\t'))
    side_c = int(input('Length of side C:\t'))
    area = (math.sqrt((side_a ** 2 + side_b ** 2 + side_c ** 2) ** 2 - 2 * (side_a ** 4 + side_a ** 4 + side_c ** 4)))/4
    print(area)

# 7. Write a Python-script that calculates the sum of the digits of a number
#    Check the task number 5.

# 8. Determine the number of digits in a number
def number_of_digits():
    number = int(input('Enter the number\t'))
    print(f'Number of digits in number {number} is {len(str(number))}')

#number_of_digits()

# 9. Print the digits in reverse order

def reversed_number():
    number = input('Enter the number to be reversed\t')
    reversed = int(number[::-1])
    print(reversed)

#reversed_number()


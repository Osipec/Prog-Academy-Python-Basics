# '''Lesson Number 3, Homework number 3. Osypenko Kostiantyn'''
#
# # 1. Write a Python program to print the number entered by user only if the
# # number entered is negative
# x = int(input('Enter the number to check if it is negative:\t'))
# b = 'The number is positive'
# a = x < 0 and x
# print(a or b)
#
# # 2. Write a Python program to check if the value a is less than 20 or not.
# value = int(input('Enter the value to check if it\'s less than 20:\t'))
# more = 'Value is more than 20'
# less = value < 20 and 'Value is less than 20'
# print(less or more)
#
# # 3. Write a Python program to check if a given number is Zero or Not.
# given_number = int(input('Let\'s check if the given number is "0" :\t'))
# yes = given_number == 0 and 'The given umber is "0"'
# less = given_number < 0 and 'The given number is less than "0"'
# more = given_number > 0 and 'The given number is bigger than "0"'
# print(yes or less or more)
#
# # 4. Write a Python program to check if a given number is Even or Odd.
# given_number = int(input('Let\'s check if the given number is Even or Odd:\t'))
# Even = given_number % 2 == 0 and 'Given number is Even'
# Odd = given_number % 2 != 0 and 'Given number is Odd'
# print(Even or Odd)
#
# # 5. Write a Python program to find largest number among three numbers
# # entered by user.
# print('\tFind the largest number among 3 of them')
# a = int(input('Enter number 1:\t'))
# b = int(input('Enter number 2:\t'))
# c = int(input('Enter number 3:\t'))
#
# x = a >= c and a >= b and a
# y = b >= c and b >= a and b
# z = c >= a and c >= b and c
# res = x or y or z
# print(f'The largest number is {res}')

number = int(input())
number < 0 and print(number)

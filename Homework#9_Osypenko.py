# Homework 9, Lesson 8, Osypenko Kostiantyn

# 1. String + number concatination
# def func(string: str, a: int, b: int):
#     return f'{string} {str(a + b)}'
# print(func('Hello', 5, 6))

# 2. Square of stars
# def square(columns: int, raws: int) -> str:
#     raw_first_last = f'{columns*"*"}'
#     raw_inside = (f'*{(columns-2)*" "}*\n')
#     final = f'{raw_first_last}\n{raw_inside * 3}{raw_first_last}'
#     return final
# print(square(6,5))

# 3. Find element in list
# import random                                                                   
# def index_finder(list_of_int: list, element: str):                              
#     if int(element) in list_of_int:                                             
#         return f'Element index is {int_list.index(int(element))}'               
#     else:                                                                       
#         return 'No such element'                                                
#                                                                                 
# int_list = [random.randint(1,101) for _ in range(100)]                          
# to_find = input('Enter element to find it\'s index:  ')                         
# while not to_find.isdigit():                                                    
#         print('Try again: ')                                                    
#         to_find = input('Enter element to find it\'s index:  ')                 
#                                                                                 
# print(index_finder(int_list, to_find))                                          

# 4. Number of words
# def words_counter(string: str) -> int:
#     new_string = ''
#     for i in string:
#         if i.isalnum() or i == ' ':
#             new_string += i
#         else:
#             new_string += ' '
#     return len(new_string.split())
#
# print(words_counter(input('Enter any sentence to count words: ')))

# 5. Price converter
# def converter(number: float):
#     nums = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
#             6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
#     decimals = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
#                 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
#     decimals_ = {2: 'twenty', 3: 'thirty', 4: 'fourty', 5: 'fifty', 6: 'sixty', 7: 'seventy',
#                  8: 'eighty', 9: 'ninety'}
#     thousands = int(number) // 1000
#     hundreds = (int(number) % 1000) // 100
#     decims = int(number) % 100
#     fraction = int(round(number - int(number), 2) * 100)
#
#     output = ''
#     if thousands:
#         output += f'{nums[thousands]} thousand '
#     if hundreds:
#         output += f'{nums[hundreds]} hundred '
#     if 10 < decims < 20:
#         output += f'{decimals[decims]} dollars '
#     elif decims >= 20:
#         output += f'{decimals_[decims // 10]} {nums[decims % 10]} dollars '
#     elif decims <= 10:
#         output += f'{nums[decims]} dollars '
#     if 10 < fraction < 20:
#         output += f'{decimals[fraction]} cents'
#     elif fraction >= 20:
#         output += f'{decimals_[fraction // 10]} {nums[fraction % 10]} cents'
#     elif 0 < fraction <= 10:
#         output += f'{nums[fraction]} cents'
#     return output.capitalize()
#
# print(converter(float(input('Enter price: '))))

# 6. Rome to arabic
# def roman_converter(roman: str) -> int | str:
#     roman_digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     while not all(map(lambda i: i in roman_digits.keys(), roman)):
#         print('Wrong input')
#         roman = (input('Enter rome number: ')).upper()
#     print(f'Your rome number is {roman}')
#     summ = 0
#     for i in range(len(roman)):
#         try:
#             if roman_digits[roman[i]] < roman_digits[roman[i + 1]]:
#                 summ -= roman_digits[roman[i]]
#             else:
#                 summ += roman_digits[roman[i]]
#         except IndexError:
#             summ += roman_digits[roman[i]]
#     return f'Converted to arabian {summ}'
#
# roman_input = (input('Enter rome number: ')).upper()
# print(roman_converter(roman_input))

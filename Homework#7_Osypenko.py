# Homework 7, Lesson 6, Osypenko Kostiantyn

# 1. Count bees)
# text = input('Enter text to count number of beez\n')
# print(text.lower().count('b'))

# 2. Name validity
# import string
# impossible_symbols = list(string.punctuation.replace('-', '').replace("'", '') + string.digits)
# string = ''
# while not string or any(i in impossible_symbols for i in string) or not string.istitle():
#     string = input('Enter the name: ')
# print('Name is correct')

# 3. Summ of symbol codes
# string = input('Enter any text: ')
# summ = sum(ord(i) for i in string)
# print(summ)

# 4. Pi untill 10 digits after dot
# from math import pi
# print(*(round(pi, i) for i in range(2, 12)), sep='\n')

# 5. Longest word in text
# text = input('Enter text:')
# longest = max(list(text.split()), key = len)
# print(longest)

    # ADDITIONAL TASKS

# 1. Vovochka
# counter_1 , counter_2, counter_3 = 1, 1, 2
# listed = []
# vova_text = input('Vova wrote: ')
# while counter_3 <= len(vova_text):
#     if vova_text[:counter_1] == vova_text[counter_2:counter_3]:
#         listed.append(vova_text[:counter_1])
#     counter_1 += 1
#     counter_2 += 1
#     counter_3 += 2
# if not listed:
#     print(vova_text)
# else:
#     for item in listed:
#         print(f'"{item}"', sep = '\t', end = ' ')
#     print()
#     print(f'Sfortest word is "{min(listed, key = len)}"')

# 2. HTML Teg Cleaner
# tagged = input('Enter or copy HTML Code: ')
# import re
# text = '<p><span>is not.      Hello world! <b><span>allowed. I like Python so much</span>Mama papa</b></span></p>'
# res = re.sub(r"<[^>]+>", ".", text, flags=re.S)
# clean = res.replace('  ', '').replace('..', '')
# print(clean)
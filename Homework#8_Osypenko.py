# Homework 8, Lesson 7, Osypenko Kostiantyn

# 1. Days of week
# days = ['Monday', 'Thuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# dict = {k: v for k, v in enumerate(days, 1)}
# key = int(input('Enter the nuber of day: '))
# print(dict.get(key, 'Days from 1 to 7'))

# 2. Cat discription
# dicted_cat = {'biological species': 'cat', 'area of living': ['home', 'street'],
#               'colour': ['ginger', 'black', 'white', 'coloured'], 'eyes colour': ['green', 'brown', 'blue']}
# raw = '\n'.join(map(lambda k: f'{k[0]}: {k[1]}', dicted_cat.items()))
# print(raw)


# 3. Letters counter
# raw = input("Enter your text here: ")
# cleaned_raw = {letter: raw.count(letter) for letter in set(raw) if letter.isalpha()}
# print(cleaned_raw)

# 4. Intersection
# raw1 = set(input('Enter raw #1: '))
# raw2 = set(input('Enter raw #2: '))
# print(raw1 & raw2)

# 5. Two lists
# list_1 = [i for i in range(50) if not i % 3]
# list_2 = [i for i in range(50) if not i % 5]
# print(list_1, list_2, sep='\n')

# 6. Intersection
# listed = (list(set(list_1) & set(list_2)))
# listed.sort()
# print(listed)

# Lesson 9, Homework 10, Osypenko Kostiantyn

# 1. Sequence finder
# import math
#
# def seq_find(sequence: str):
#     new_seq = tuple(map(int, sequence.replace(',', ' ').split()))
#     # print(new_seq)
#     c = new_seq[-1]
#     b = new_seq[-2]
#     a = new_seq[-3]
#     res = seq_1(a, b, c) or seq_2(a, b, c) or seq_3(a, b, c) or \
#           seq_4(a, b, c) or seq_5(a, b, c) or seq_6(a, b, c)
#     return res
# '''Functions below discribe sequence and returns next element. If you want to add a new sequence
# write a function and add it's call in line 13. Parameters a, b, c are three last elements of sequence,
# d is the element to find. New function should return d if a, b, c satisfy regularity of sequence, if not, return False'''
# def seq_1(a: int, b: int, c: int):
#     if a + 2 == b and b + 2 == c:
#         d = c + 2
#         return d
#     else:
#         return False
#
# def seq_2(a: int, b: int, c: int):
#     if a + 3 == b and b + 2 == c:
#         d = c + 3
#         return d
#     else:
#         return False
#
# def seq_3(a: int, b: int, c: int):
#     if a * 2 == b and b * 2 == c:
#         d = c * 2
#         return d
#     else:
#         return False
#
# def seq_4(a: int, b: int, c: int):
#     if a * 3 == b and b * 3 == c:
#         d = c * 3
#         return d
#     else:
#         return False
#
# def seq_5(a: int, b: int, c: int):
#     if (c - b) - (b - a) == 2:
#         d = c + (c - b) + 2
#         return d
#
# def seq_6(a: int, b: int, c: int):
#     if math.ceil(c ** (1 / 3)) - math.ceil(b ** (1 / 3)) == 1 and math.ceil(b ** (1 / 3)) - math.ceil(a ** (1 / 3)) == 1:
#         d = (math.ceil(c ** (1 / 3)) + 1) ** 3
#         return d
#     else:
#         return False
#
# print(seq_find(input('Enter sequence to find next element:\n')) or 'No sequence in data base')

# 2. Palindrome
# pali = max(set(((a * b), a, b) for a in range(9000, 10000) for b in range(9000, 10000) if str(a*b) == str(a*b)[::-1]))
# print(f'Max palindrome is {pali[0]}, a = {pali[1]}, b = {pali[2]}')
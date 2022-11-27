# Lesson 9, Homework 10, Osypenko Kostiantyn

# 1. Sequence finder
import math


def seq_find(sequence: str, func):
    new_seq = tuple(map(int, sequence.replace(',', ' ').split()))
    return func(new_seq)


def seq_1_plus_2(seq):
    for i in range(len(seq) - 1):
        if seq[i + 1] != seq[i] + 2:
            return "Sequence Error"
    else:
        return seq[-1] + 2


def seq_2_plus_3(seq):
    for i in range(len(seq) - 1):
        if seq[i + 1] != seq[i] + 3:
            return "Sequence Error"
    else:
        return seq[-1] + 3


def seq_3_multy_2(seq):
    for i in range(len(seq) - 1):
        if seq[i + 1] != seq[i] * 2:
            return "Sequence Error"
    else:
        return seq[-1] * 2


def seq_4_multy_3(seq):
    for i in range(len(seq) - 1):
        if seq[i + 1] != seq[i] * 3:
            return "Sequence Error"
    else:
        return seq[-1] * 3


def seq_5_plus_odd(seq):
    for i in range(len(seq) - 1):
        if not (seq[i + 1] - seq[i]) % 2:
            return "Sequence Error"
    else:
        return seq[-1] + (seq[-1] - seq[-2] + 2)


def seq_6_pow_3(seq):
    for i in range(len(seq) - 1):
        if math.ceil(seq[i + 1] ** (1 / 3)) - math.ceil(seq[i] ** (1 / 3)) != 1:
            return "Sequence Error"
    else:
        return (math.ceil(seq[-1] ** (1 / 3)) + 1) ** 3


input_seq = input('Enter sequence: ')
print(seq_find(input_seq, seq_1_plus_2))

# 2. Palindrome
# import time
# start = time.time()
# pali = max(list(((a * b), a, b) for a in range(100_000, 99_000, -1) for b in range(100_000, 99_000, -1)
#                 if str(a * b) == str(a * b)[::-1]))
# print(f'Max palindrome is {pali[0]}, a = {pali[1]}, b = {pali[2]}')
# end = time.time() - start
# print(end)

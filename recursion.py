#!/usr/bin/env python

"""
Дана последовательность целых чисел, заканчивающаяся числом 0.
Выведите эту последовательность в обратном порядке.

решение для: https://pythontutor.ru/lessons/functions/problems/reverse_rec/
"""


def reverse(n):
    """
    Решение задачи рекурентно.
    :param n:
    :return:
    """
    if n == 0:
        print(f"{n}")
    else:
        reverse(int(input()))
        print(f"{n}")


if __name__ == "__main__":
    reverse(int(input()))
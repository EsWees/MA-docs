#!/usr/bin/env python

# Need for be able use stderr and stdout
import sys

""" Realize convert functional from int or float to words """


def print_converted(to_words):
    """The function do convert from int or float to words"""
    less_then_10 = {
        0: "ноль",
        1: "одна",
        2: "две",
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь",
        8: "восемь",
        9: "девять"
    }

    grater_then_10 = {
        11: "одинадцать",
        12: "двенадцать",
        13: "тринадцать",
        14: "четырнадцать",
        15: "пятнадцать",
        16: "шестнадцать",
        17: "семьнадцать",
        18: "восемьнадцать",
        19: "девятнадцать"
    }

    dozens = {
        10: "десять",
        20: "двадцать",
        30: "тридцать",
        40: "сорок",
        50: "пятьдесят",
        60: "шестьдесят",
        70: "семьдесят",
        80: "восемьдесят",
        90: "девяносто"
    }

    hundreds = {
        100: "сто",
        200: "двести",
        300: "триста",
        400: "четыреста",
        500: "пятьсот",
        600: "шестьсот",
        700: "семьсот",
        800: "восемьсот",
        900: "девятьсот"
    }

    try:
        to_words = float(to_words)
    except ValueError as value_err:
        print(f"Скрипт не поддерживает данный символ: {value_err}", file=sys.stderr)
        exit(1)

    grn = int(to_words - to_words % 1)
    kop = int((to_words % 1) * 100)

    ## DEBUG
    # print(f"{grn=}, {kop=}")

    def convert(x, i=10):
        if x in less_then_10:
            if x == 0:
                pass
            else:
                print(less_then_10[x], end=" ")
                return x
        elif (x // 100) * 100 in hundreds:
            print(hundreds[(x // 100) * 100], end=" ")
            convert(x % 100)
            return x
        elif x in grater_then_10 and 11 <= x <= 19:
            print(grater_then_10[x], end=" ")
            convert(x % x)
            return x
        elif (x // 10) * 10 in dozens:
            print(dozens[(x // 10) * 10], end=" ")
            convert(x % 10)
            return x
        else:
            convert(int(x / i))
            ## DEBUG
            # print(f"convert(int({x / i})")

    # TODO: реализовать вывод слов
    # 1 тысяча
    # 2-4 тысячи
    # 5 тысяч
    convert(grn)
    # гривны, гривен, гривна
    convert(kop)
    # копейка, копеек, копейки
    print() # empty line ;)


try:
    print(f"Надо писать всякую хрень:", end=" ", file=sys.stdout)
    user_input = float(input())
except ValueError as value_err:
    print(f"Скрипт не поддерживает данный символ: {value_err}", file=sys.stderr)
    exit(1)

print_converted(user_input)
print()

print_converted("9.99")
print_converted("194.99")
print_converted("10.50")
print_converted("12.43")
print_converted("22.30")
print_converted("300000.00")

# TODO: need a fix when x less than 0
print_converted("-26.36")  ## Какая-то лажа

print_converted("6.17")
print_converted("9.81")
print_converted("5.62")

print_converted("d")

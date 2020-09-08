#!/usr/bin/env python

# Need for be able use stderr and stdout
import sys

""" Realize convert functional from int or float to words """

def print_converted(to_words):
    """The function do convert from int or float to words"""
    print(to_words, end=" ")

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
        assert 0 < to_words < 10000, "Input must be grater then zero"
    except AssertionError as value_err:
        raise value_err
    except ValueError as value_err:
        print(f"Скрипт не поддерживает данный символ: {value_err}", file=sys.stderr)
        return

    grn = int(to_words - to_words % 1)
    kop = int(round((to_words % 1), 2) * 100)

    assert kop < 100, "Та быть не может... Копеек бывает масимум 99"

    # DEBUG
    #print(f"{grn=}, {kop=}")

    def convert(x, i=10):
        if x in less_then_10:
            if x == 0:
                pass
            else:
                print(less_then_10[x], end=" ")
                return x
        elif (x // 1000) in less_then_10 and x > 1000:
            print(less_then_10[(x // 1000)], end=" ")
            if x // 1000 == 1 or x // 1000 % 10 == 1:
                print("тысяча", end=" ")
            elif 1 < x // 1000 < 5 or 2 <= x // 1000 % 10 <= 4:
                print("тысячи", end=" ")
            else:
                print("тысяч", end=" ")
            convert(x % 1000)
            return x
        elif (x // 100) * 100 in hundreds:
            print(hundreds[(x // 100) * 100], end=" ")
            convert(x % 100)
            return x
        elif x in grater_then_10 and 11 <= x <= 19:
            print(grater_then_10[x], end=" ")
            convert(x % 1)
            return x
        elif (x // 10) * 10 in dozens:
            print(dozens[(x // 10) * 10], end=" ")
            convert(x % 10)
            return x
        else:
            convert(int(x / i))
            ## DEBUG
            print("more convert")

    convert(grn)
    if (grn == 1 or grn % 10 == 1) and 10 < grn > 20:
        print("гривна", end=" ")
    elif (1 < grn < 5 or 2 <= grn % 10 <= 4) and 10 < grn > 20:
        print("гривны", end=" ")
    elif grn == 0:
        print("ноль гривен", end=" ")
    else:
        print("гривен", end=" ")

    convert(kop)
    if (kop == 1 or kop % 10 == 1) and 10 < kop > 20:
        print("копейка")
    elif (1 < kop < 5 or 2 <= kop % 10 <= 4) and 10 < kop > 20:
        print("копейки")
    elif kop == 0:
        print("ноль копеек")
    else:
        print("копеек")
    print() # empty line ;)


def test():
    try:
        print(f"Please type here a number:", end=" ", file=sys.stdout)
        user_input = float(input())
    except ValueError as value_err:
        pass
        print(f"This is script does not support a charsets: {value_err}", file=sys.stderr)
        return
    print_converted(user_input)
    print()


if __name__  ==  "__main__":
    test()

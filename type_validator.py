#!/usr/bin/env python

def validator(*args):
    def val_decorator(func):
        def func_wrapper(*func_args):
            for a, b in zip(func_args, args):
                if type(a) is b:
                    print(f"{a=},{b=}")
                    return func(*func_args)
                else:
                    raise ValueError("type error")
        return func_wrapper
    return val_decorator


@validator(int, list)
def some_fun(a, b):
    return a, b


@validator(float, int)
def some_fun2(a, b):
    return a, b


some_fun(2, [1,3,4,5])
some_fun2(0.2, 1)

#some_fun2(2, 8)
"""
Traceback (most recent call last):
  File "/home/eswees/Documents/PyHead/MainAcadeny-Python/type_validator.py", line 29, in <module>
    some_fun2(2, 8)
  File "/home/eswees/Documents/PyHead/MainAcadeny-Python/type_validator.py", line 11, in func_wrapper
    raise ValueError("type error")
ValueError: type error
"""
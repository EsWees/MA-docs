#!/usr/bin/env python3

# Implement functions that
# - return True if the input string contains a float number
# - return False in the other case
"ttttt 0.25 sdfiusdfsdf"

def is_float_decorator(func):
    def wrapper(args):
        if func(args): 
            return True
        elif func(float(args)):
            return True
        else:
            return False
    return wrapper


def is_float_with_except_decorator(func):
    def wrapper(args):
        return args if func(args) else False
    return wrapper


@is_float_with_except_decorator
def is_float_with_except(str_int):
    try:
        if type(str_int) == float:
            return True
        elif type(float(str_int)) == float:
            return True
        else:
            return False
    except ValueError:
        return False
    except Exception as error:
        print(f"Exception {error.__class__.__name__}, {error}")
        return error


@is_float_decorator
@is_float_with_except
def is_float(str_int):
    if type(str_int) is float:
        return True
    else:
        return False


def check_is_float(check_fun):
    assert check_fun(2.56)
    assert check_fun("340.5")
    assert check_fun("+23")
    assert check_fun("-231")
    assert not check_fun("-23y1")
    assert not check_fun("abc")

check_is_float(is_float)
check_is_float(is_float_with_except)

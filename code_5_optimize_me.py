#!/usr/bin/env python

def testing_function():
    test = 0
    def calc():
        nonlocal test
        test += 1
        return test
    return calc

iteration = testing_function()

for i in range(0, 10):
    print(f'{iteration()}')

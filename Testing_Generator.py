#!/usr/bin/env python


foo = ["A", "B", "C", "D", "E"]


def my_enumerate(lst):  # Define own enumerate function
    for item in lst:  # Loop for generation objects with yield
        yield lst.index(item) + 1, item  # Return tuple with 2 items - item index +1 and item value


for item in my_enumerate(foo):
    print(item)

for i, item in enumerate(foo, 1):
    print(f"{i=}, {item=}")

f = my_enumerate(foo)
while True:
    try:
        print(next(f))
    except StopIteration as err:
        print(f"Done {err.__class__.__name__}")
        break
    finally:
        print(f"OOOPS")

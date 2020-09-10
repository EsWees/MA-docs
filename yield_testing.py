#!/usr/bin/env bash


def yield_testing():
    i = 0
    while i < 2:
        print(f"Before")
        yield i
        print(f"After")
        i += 1


f = yield_testing()

print(f"{id(f)=}")
print(next(f))
print(next(f))
print(next(f))
print(list(f))
"""
Traceback (most recent call last):
  File "/home/eswees/.../yield_testing.py", line 18, in <module>
    print(next(f))
StopIteration
"""

print(next(f))
print(next(f))

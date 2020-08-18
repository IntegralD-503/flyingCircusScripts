#!/usr/bin/env python3
def sub(a,b):
  print(a-b)

def smart_sub(func):
    def inner(a,b):
        if a < b:
            a, b = b, a
        return func(a,b)
    return inner

sub = smart_sub(sub)

sub(1,6)

#!/usr/bin/env python

curr = input()
prev = 0

i = 0
while i < 5:
    n = input()

    if n < curr:
        print "lower"
    elif n == curr:
        print "equal"
    else:
        print "higher"
    curr = n
    i = i + 1

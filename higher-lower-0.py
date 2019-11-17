#!/usr/bin/env python

curr = input()
prev = 0
n = 1

while n != 0:
    n = input()
    if n < curr:
        print "lower"
    elif n == curr:
        print "equal"
    else:
        print "higher"
    curr = n

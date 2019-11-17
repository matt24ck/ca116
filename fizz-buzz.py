#!/usr/bin/env python

n = input()
i = 0
while i < n:
    if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
        print "fizz-buzz"
    elif (i + 1) % 5 == 0:
        print "buzz"
    elif (i + 1) % 3 == 0:
        print "fizz"
    else:
        print i + 1
    i = i + 1

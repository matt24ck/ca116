#!/usr/bin/env python

import sys
a = []

s = raw_input()
while s != "end":
    a.append(s)
    s = raw_input()

i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        if (a[i])[j - len(sys.argv[1]):j] == sys.argv[1]:
            print a[i]
        elif len(sys.argv) == 1:
            print a[i]
        j += 1
    i += 1


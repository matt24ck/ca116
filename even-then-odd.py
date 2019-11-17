#!/usr/bin/env python

s = raw_input()
a = []
b = []
while s != "end":
    if int(s) % 2 == 0:
        a.append(int(s))
    else:
        b.append(int(s))
    s = raw_input()
i = 0
while i < len(a + b):
    print (a + b)[i]
    i += 1

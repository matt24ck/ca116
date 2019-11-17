#!/usr/bin/env python

s = raw_input()
a = []
while s != "end":
    a.append(s)
    s = raw_input()

t = raw_input()
b = []
while t != "end":
    b.append(int(t))
    t = raw_input()

i = 0
while i < len(b):
    print a[b[i]]
    i += 1

#!/usr/bin/env python

a = []
s = raw_input()
while s != "end":
    a.append(int(s))
    s = raw_input()
n = input()
a.append(n)

i = 1
while i < len(a):
    p = i
    v = a[i]
    while 0 < p and v < a[p - 1]:
        a[p] = a[p - 1]
        p -= 1
    a[p] = v
    i += 1

print a

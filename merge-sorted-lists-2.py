#!/usr/bin/env python

a = []
s = raw_input()
while s != "end":
    a.append(int(s))
    s = raw_input()
b = []
t = raw_input()
while t != "end":
    b.append(int(t))
    t = raw_input()
c = a + b
i = 0
while i < len(c):
    j = i + 1
    p = i
    while j < len(c):
        if c[j] < c[p]:
            p = j
        j += 1

    tmp = c[i]
    c[i] = c[p]
    c[p] = tmp
    i += 1
k = 0
while k < len(c):
    print c[k]
    k += 1

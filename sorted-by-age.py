#!/usr/bin/env python

a = []

s = raw_input()
while s != "end":
    a.append(s)
    s = raw_input()

i = 0
while i < len(a):
    j = i + 1
    p = i
    while j < len(a):
        if int((a[j])[6:8]) < int((a[p])[6:8]):
            p = j
        elif int((a[j])[3:5]) < int((a[p])[3:5]):
            p = j
        elif int((a[j])[0:2]) < int((a[p])[0:2]):
            p = j
        j += 1

    tmp = a[i]
    a[i] = a[p]
    a[p] = tmp
    i += 1
k = 0
while k < len(a):
    print a[k][9:]
    k += 1

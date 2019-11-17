#!/usr/bin/env python

a = []
s = raw_input()
while s != "end":
    a.append(int(s))
    s = raw_input()

i = 0
total = 0
while i < len(a):
    total = total + a[i]
    i += 1
if len(a) > 0:
    avg = float(total / len(a))
j = 0
while j < len(a):
    if len(a) > 0 and a[j] > avg:
        print a[j]
    j += 1

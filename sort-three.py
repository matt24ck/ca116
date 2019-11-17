#!/usr/bin/env python

a = []
i = 0

n = input()
m = input()
o = input()

if n <= m and m <= o:
    a = [n, m, o]
elif n <= o and o <= m:
    a = [n, o, m]
elif m <= n and n <= o:
    a = [m, n, o]
elif m <= o and o <= n:
    a = [m, o, n]
elif o <= m and m <= n:
    a = [o, m, n]
else:
    a = [o, n, m]

i = 0
while i < len(a):
    print a[i]
    i += 1

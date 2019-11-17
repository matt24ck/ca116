#!/usr/bin/env python

n = input()

x = range(1, n + 1)
pot_factors = list(x)
y = []
for item in pot_factors:
    if n % item == 0:
        y.append(item)

if len(y) == 2:
    print "prime"
else:
    print "not prime"
    
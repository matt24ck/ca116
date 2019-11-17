#!/usr/bin/env python

i = 0
posTotal = 0
negTotal = 0

while i < 5:
    n = input()
    if n < 0:
        negTotal = negTotal + n
    else:
        posTotal = posTotal + n
    i = i + 1
print negTotal, posTotal

#!/usr/bin/env python

n = 1
posTotal = 0
negTotal = 0

while n != 0:
    n = input()
    if n < 0:
        negTotal = negTotal + n
    else:
        posTotal = posTotal + n

print negTotal, posTotal

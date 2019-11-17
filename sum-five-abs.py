#!/usr/bin/env python

m = 1
total = 0
while m != 0:
    m = input()
    if m < 0:
        m = -1 * m
    total = total + m
print total

#!/usr/bin/env python

n = 1
prev = 0
curr = 0
while n != 0:
    n = input()
    curr = n
    curr = curr + prev
    prev = curr
print prev

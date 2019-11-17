#!/usr/bin/env python

i = 0
curr = 0
prev = 0
while i < 5:
    m = input()
    curr = m
    curr = curr + prev
    prev = curr
    i = i + 1
print prev

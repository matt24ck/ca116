#!/usr/bin/env python

s = raw_input()
i = 0
total = 0

while i < len(s):
    if s[i] == 1:
        total = total * 2 + 1
    else:
        total = total * 2
    i = i + 1
print total 

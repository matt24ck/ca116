#!/usr/bin/env python

i = 0
s = raw_input()
t = ""
while i < len(s):
    x = s[len(s) - 1 - i]
    t = t + x
    i = i + 1
print t

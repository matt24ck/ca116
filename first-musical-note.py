#!/usr/bin/env python

s = raw_input()
i = 0
t = ""
while i < len(s) and 1 > len(t):
    if s[i] == "a":
        t = t + s[i]
    elif s[i] == "b":
        t = t + s[i]
    elif s[i] == "c":
        t = t + s[i]
    elif s[i] == "d":
        t = t + s[i]
    elif s[i] == "e":
        t = t + s[i]
    elif s[i] == "f":
        t = t + s[i]
    elif s[i] == "g":
        t = t + s[i]
    i = i + 1

print t

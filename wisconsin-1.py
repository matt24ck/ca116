#!/usr/bin/env python

i = 0
s = raw_input()
while s != "end":
    i = 0
    while i < len(s) and s[i] != ",":
        i += 1
    if s[i + 1:i + 3] == "WI":
        print s[:i]
    s = raw_input()

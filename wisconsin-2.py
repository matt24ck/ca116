#!/usr/bin/env python

i = 0
count = 0
s = raw_input()
while s != "end":
    i = 0
    while i < len(s) and s[i] != ",":
        i += 1
    if s[i + 1:i + 3] == "WI":
        count += 1
    s = raw_input()
print count

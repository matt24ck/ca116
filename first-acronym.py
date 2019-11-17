#!/usr/bin/env python

s = raw_input()
i = 0

while i < len(s) and ("A" > s[i] or s[i] > "Z"):
    i += 1
if i < len(s):
    j = i
    while j < len(s) and ("A" <= s[j] and s[j] <= "Z"):
        j += 1

    print s[i:j], i

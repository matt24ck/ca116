#!/usr/bin/env python

s = raw_input()
i = 0
n = ""
while i < len(s) and 1 > len(n):
    if s[i] != s[i].lower():
        n = n + s[i]
        print i
    i = i + 1

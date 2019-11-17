#!/usr/bin/env python

upper = "ABCDEFGHIFKLMNOPQRSTUVWXYZ"
lower = "abcdefghifklmnopqrstuvwxyz"

i = 0
s = raw_input()
while s != "end":
    i = 0
    while i < len(s) and i < len(upper):
    	if s[i] 
        i += 1
    j = 1
    while j < len(s) and j > 0 and s[(len(s) - j)] != ":":
        j += 1
    print s[:i], s[(len(s) - j) + 1:]
    s = raw_input()
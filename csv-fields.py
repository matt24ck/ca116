#!/usr/bin/env python

import sys
a = []
start = 0
s = raw_input()
i = 0
while i < len(s) and (("a" <= s[i] and s[i] <= "z") or ("A" <= s[i] and s[i] <= "Z") or( s[i] == ",")):
    end = start
    while end < len(s) and s[end] != ",":
        end += 1  
    a.append(s[start:end])
    start = end + 1
    i += 1

print a[int(sys.argv[1])]
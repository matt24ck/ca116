#!/usr/bin/env python

i = 0
s = raw_input()
total = 0
while i < 5:
    j = 0
    k = 0
    while k < len(s) and s[k] != "+":
        total = total + int(s[j:k])
        
        k += 1
    else:
        j = k
    print s[j:k]
    i += 1
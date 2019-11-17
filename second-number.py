#!/usr/bin/env python

s = raw_input()
i = 0

while i < len(s) and ("0" > s[i] or s[i] > "9"):
    i += 1
if i < len(s):
    j = i
    while j < len(s) and ("0" <= s[j] and s[j] <= "9"):
        j += 1
    if j < len(s):
        k = j
        while k < len(s) and ("0" > s[k] or s[k] > "9"):
            k += 1
        if k < len(s):
            l = k
            while l < len(s) and ("0" <= s[l] and s[l] <= "9"):
                l += 1
            print s[k:l], k

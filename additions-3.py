#!/usr/bin/env python

mySum = 1

while mySum != 1000:
    s = raw_input()
    j = 0
    while j < len(s) and s[j] != "+":
        j += 1
    mySum = int(s[:j]) + int(s[j:])
    print mySum

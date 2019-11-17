#!/usr/bin/env python

import sys
args = int(sys.argv[1])
a = []
start = 0
s = raw_input()
i = 0
while i < args + 1:
    end = start
    while end < len(s) and s[end] != ",":
        end += 1
    a.append(s[start:end])
    start = end + 1
    i += 1

print a[args]

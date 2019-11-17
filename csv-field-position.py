#!/usr/bin/env python

import sys
arg = sys.argv[1]
a = []
s = raw_input()
i = 0
start = 0

while i < len(s):
    end = start
    while end < len(s) and s[end] != ",":
        end += 1
    a.append(s[start:end])
    start = end + 1
    i += 1

j = 0
while j < len(a):
    if a[j] == arg:
        print j
    j += 1

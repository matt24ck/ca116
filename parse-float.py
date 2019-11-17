#!/usr/bin/env python

f = raw_input()
i = 0

while i < len(f) and f[i] != ".":
    i += 1
if i < len(f):
    j = i
    while j < len(f) and f[j] == ".":
        j += 1

    print f[0:i]
    print f[j:]

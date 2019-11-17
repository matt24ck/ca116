#!/usr/bin/env python

i = 0
s = raw_input()
t = ""
while s != "end":
    while i < len(s) and s[i] != " ":
        i += 1
    print s[:i]
    s = raw_input()
a = []
u = raw_input()
while u != "end":
    if s[:i] == u:
        a.append(u)

k = 0
while k < len(a):
    print a[k]
    k += 1

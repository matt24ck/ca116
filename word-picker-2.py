#!/usr/bin/env python

s = raw_input()
a = []
while s != "end":
    a.append(s)
    s = raw_input()

s = raw_input()
total = ""
while s != "end":
    if s == "":
        total += "\n"
    else:
        s = int(s)
        total += a[s] + " "
    s = raw_input()
print total[:len(total) - 1]

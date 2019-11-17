#!/usr/bin/env python

s = raw_input()
a = []
while s != "end":
    a.append(s)
    s = raw_input()

t = raw_input()
b = []
while t != "end":
    b.append(t)
    t = raw_input()
c = []
u = ""
i = 0
while i < len(b):
	if len(b[i]) > 0:
		u += a[int(b[i])] + " "
	else:
		u += "\n"
	i += 1
print u
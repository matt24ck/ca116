#!/usr/bin/env python

x1 = input()
y1 = input()
r1 = input()

x2 = input()
y2 = input()
r2 = input()

if (r1 + r2) > (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5:
    print "yes"
else:
    print "no"

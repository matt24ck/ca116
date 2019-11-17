#!/usr/bin/env python

a = input()
b = input()
c = input()

if a >= b + c:
    print "no"
elif b >= a + c:
    print "no"
elif c >= a + b:
    print "no"
else:
    print "yes"

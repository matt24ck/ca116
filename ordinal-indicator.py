#!/usr/bin/env python

n = input()

if n == 11 or n == 12 or n == 13:
    print "th"
elif (n - 1) % 10 == 0:
    print "st"
elif (n - 2) % 10 == 0:
    print "nd"
elif (n - 3) % 10 == 0:
    print "rd"
else:
    print "th"

#!/usr/bin/env python

n = input()

if n == 1:
    print "not prime"
elif n == 2 or n == 3 or n == 5:
    print "prime"
elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
    print "not prime"
else:
    print "prime"

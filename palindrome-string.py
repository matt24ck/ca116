#!/usr/bin/env python

w = raw_input()
i = 0

while i < len(w) and w[i] == w[len(w) - i - 1]:
    i += 1
if i == len(w):
    print "palindrome"

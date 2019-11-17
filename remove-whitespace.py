#!/usr/bin/env python

s = raw_input()
i = 0
t = ""
x = ""
while i < len(s):
	if s[i] == " ":
		t = t
	else:
		t = s[i]
	y = x + t
	i = i + 1
print y

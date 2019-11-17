#!/usr/bin/env python

a = []

s = raw_input()
while s != "end":
    a.append(s)
    s = raw_input()
new_list = []
i = 0
while i < len(a):
    if a[i] not in new_list:
        new_list.append(a[i])
    i += 1
j = 0
while j < len(new_list):
    print new_list[j]
    j += 1

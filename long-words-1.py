#!/usr/bin/env python

if __name__ == "__main__":
    a = ["dog", "", "cat", "mouse", "elephant"]

count = 0
i = 0
while i < len(a):
    if len(a[i]) > 5:
        print a[i]
    i += 1

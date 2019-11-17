#!/usr/bin/env python

if __name__ == "__main__":
    a = [8, 9, 4, 7, 2, 11]


a.append(a[0])
a[0] = a[len(a) - 2]
a.pop(len(a) - 2)

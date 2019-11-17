#!/usr/bin/env python

date = raw_input()
i = 0

while i < len(date) and date[i] != " ":
    i += 1
if i < len(date):
    j = i
    while j < len(date) and j == " ":
        j += 1
    if j < len(date):
        k = j
        while k < len(date) and k != " ":
            k += 1
        if k < len(date):
            l = k
            while l < len(date) and l == " ":
                l += 1
            if l < len(date):
                m = l
                while m < len(date) and m != ",":
                    m += 1
                if m < len(date):
                    n = m
                    while n < len(date) and ("a" > s[i] or s[i] > "z") or ("A" > s[i] or s[i] > "Z"):
                        n += 1
                    if n < len(date):
                        o = n
                        while o < len(date) and "0" <= o and o <= "9":
                            o += 1

                        if o > len(date):
                            print date[l:m] + date[j:k] + "," + date[n:o] + "(" + date[i:j] + ")"
                                                 
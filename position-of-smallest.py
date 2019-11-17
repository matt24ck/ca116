#!/usr/bin/env python

if __name__ == "__main__":
    a = [4595, 6620, 10782, 9411, 30641, 20664, 14408]

end = 0

if len(a) == 1 or a[0] < a[1]:
    end = 0
else:
    end = 1

i = 2
while i < len(a):
    if a[i] < a[end]:
        end = i
    i += 1

print end

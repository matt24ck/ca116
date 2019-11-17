#!/usr/bin/env python

test_list = [1, 2, 3, 2, 3, 4, 5, 4]

new_list = []
i = 0
while i < len(test_list):
	if test_list[i] not in new_list:
		new_list.append(test_list[i])
	i += 1

print new_list
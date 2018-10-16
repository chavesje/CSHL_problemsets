#!/usr/bin/env python3
import sys
ten = int(sys.argv[1])

if ten < 0:
	print('negative')

elif ten > 0:
	print('positive')
	if ten < 50:
		print('less than 50')
else:
	print('zero')


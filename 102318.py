#!/usr/bin/env python3
import sys


number = int(sys.argv[1])

if number < 50:
	answer = "less than 50"
	print(answer)
if number < 20:
	answer = 'less than 30'
	print(answer)
if number < 0:
	answer = 'negative'
	print(answer)
else:
	answer = 'greater than or equal to 50'
	print(answer)



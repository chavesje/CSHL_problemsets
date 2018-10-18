#!/usr/bin/env python3
import re


fo = open('Python_07_nobody.txt', 'r')

for line in fo:
	#print(line)
	found=re.search(r"Nobody",line)
	print(found)

fo.close()



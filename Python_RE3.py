#!/usr/bin/env python3

fo = open('Python_07.fasta','r')
import re

for line in fo:
	found=re.findall(r">.+S",line)
	print(found)

fo.close()
	

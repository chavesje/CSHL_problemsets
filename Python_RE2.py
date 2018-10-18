#!/usr/bin/env python3
import re

fo = open('Python_07_nobody.txt','r') 

for line in fo:
	fo_sub=re.sub(r'Nobody','Ian',line)
	print(fo_sub)

fo.close()


	

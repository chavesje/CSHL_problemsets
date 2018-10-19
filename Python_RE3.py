#!/usr/bin/env python3

fo = open('Python_07.fasta','r')
import re

for line in fo:
	Extracted_seq_name=re.findall(r"^>(\S+)\s",line)
	if Extracted_seq_name:
		print(Extracted_seq_name)

fo.close()
	

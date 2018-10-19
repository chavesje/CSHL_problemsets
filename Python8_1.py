#!/usr/bin/env python3

fasta = open('Python_08.fasta', 'r')

for line in fasta:
	if '>' in line:
		print("gene name:",line)

	else:
		print("sequence:",line)

fasta.close()

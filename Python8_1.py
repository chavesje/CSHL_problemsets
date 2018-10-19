#!/usr/bin/env python3

#fasta = open('Python_08.fasta', 'r')
fasta = open('simplefasta.fa', 'r')

fasta_dict = {}

for line in fasta:
	line=line.rstrip()
	if line.startswith('>'):
		header = line
		fasta_dict[header]= 'nothing yet'
	else:
		seq = line
		fasta_dict[header]= seq


print(fasta_dict)		

fasta.close()

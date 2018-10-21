#!/usr/bin/env python3
from Bio import SeqIO


fasta_dict = SeqIO.to_dict(SeqIO.parse('ngsworkshop/input_files/human_cds.fasta', 'fasta'))
print(fasta_dict)	
	



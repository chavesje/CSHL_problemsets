#!/usr/bin/env python3
import sys

#capture command line arguments
#kmer_length = sys.argv[1]
filename_fastq = sys.argv[1]
#num_top_kmers = sys.argv[3]

kmer_dict = {}

with open(filename_fastq,"r") as file_obj:
	count = 1

	for line in file_obj:
		if count == 5:
			count = 1
		line = line.rstrip()
		if count == 2:               #alternative: if counter 4 == 2:  
			count k_mers(kmer_dict, kmer_length, sequence):
		count += 1

def k_mers(kmer_dict, kmer_length, sequence):
	for i in range(0, len(sequence) - kmer_length +1):
		kmer = sequence[i:(i+kmer_length)] #extract the kmer as a substring
	

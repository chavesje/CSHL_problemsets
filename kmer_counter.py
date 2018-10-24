#!/usr/bin/env python3
import sys

#capture command line arguments
kmer_length = sys.argv[1]
filename_fastq = sys.argv[2]
#num_top_kmers = sys.argv[3]

kmer_dict = {}
kmer_list = []

with open(filename_fastq,"r") as file_obj:
	
	count = 1
	for line in file_obj:
		if count == 5:
			count = 1
		line = line.rstrip()
		if count == 2:               #alternative: if counter 4 == 2:  
			for i in range(0,len(line) - int(kmer_length) +1):
				kmer = line[i:(i+int(kmer_length))]
				kmer_list.append(kmer)
		count += 1
	
#print(kmer_list)

for kmer in kmer_list:
	if kmer in kmer_dict:
		kmer_dict[kmer] += 1
	else:
		kmer_dict[kmer]= 1

#print(kmer_dict)

#for key, value in kmer_dict.items():
#	sorted_dict = sorted(value)

print(sorted(kmer_dict.values(reverse=True)))

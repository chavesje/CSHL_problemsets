#!/usr/bin/env python3

import sys
transcript_file = sys.argv[1]

Transcript_dict = {}


with open(transcript_file,'r') as file_obj:
	for line in file_obj:
		line = line.rstrip()
		line_split = line.split("\t")
		transcript_num = line_split[0]
		gene = line_split[2] 
		gene_name = gene.split("^")[0]

		if gene_name in Transcript_dict: 
			Transcript_dict[gene_name].add(transcript_num)			

		else:
			Transcript_dict[gene_name]= set([transcript_num])

	for gene_name in Transcript_dict:
		# value = dict[key]
		reads = Transcript_dict[gene_name]
		print(gene_name,len(reads))
	




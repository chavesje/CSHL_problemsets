#!/usr/bin/env python3

class DNARecord(object):

	sequence = 'AAAAATTTTTCCCCCGGGGGGGG'
	gene_name = 'IspS'
	organism = 'P. montana'

	def __init__(self, seq='', gene_name=None, organism=None):
		self.sequence = seq
		self.gene_name = gene_name
		self.organism = organism

sequence = 'AAAAATTTTTCCCCCGGGGGGGG'
gene_name = 'IspS'
organism = 'P. montana'
dna_rec_obj = DNARecord(sequence, gene_name, organism)
dna_rec_obj2 = DNARecord()
print(dna_rec_obj2.sequence)
dna_rec_obj2.sequence = 'ggggg'
print(dna_rec_obj2.sequence)
print(dna_rec_obj.gene_name)
print(dna_rec_obj.sequence)
dna_rec_obj2 = DNARecord()
print(dna_rec_obj2.sequence)


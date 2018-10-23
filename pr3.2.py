#!/usr/bin/env python3

import sys

dna = sys.argv[1]

A = dna.count('A')
T = dna.count('T')
dna_len = len(dna)

AT_content =( (A + T) / dna_len)
print(AT_content)

 

#!/usr/bin/env python3

import sys

dna = sys.argv[1]

dna_rev = dna[::-1]
dna_rev_lower = dna_rev.lower()
rc_1 = dna_rev_lower.replace('a','T')
rc_2 = rc_1.replace('t','A')
rc_3 = rc_2.replace('g','C')
rc_4 = rc_3.replace('c','G')

print(rc_4)





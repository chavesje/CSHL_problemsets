#!/usr/bin/env python3

#problem set IV

In [59]: taxa = 'sapiens, erectus, neanderthalensis'

In [60]: print(taxa)
sapiens, erectus, neanderthalensis

In [61]: print(taxa[1])
a

In [62]: type(taxa)
Out[62]: str

In [63]: taxa.split(',')
Out[63]: ['sapiens', ' erectus', ' neanderthalensis']

In [64]: species = taxa.split(',')

In [65]: print(species)
['sapiens', ' erectus', ' neanderthalensis']

In [66]: type(species)
Out[66]: list

In [67]: sorted(species)
Out[67]: [' erectus', ' neanderthalensis', 'sapiens']

In [68]: sorted(species, key=len)
Out[68]: ['sapiens', ' erectus', ' neanderthalensis']

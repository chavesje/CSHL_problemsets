#!/usr/bin/env python3
import sys
DNA_two = sys.argv[1]



A = DNA_two.count ('A')
T = DNA_two.count ('T')
G = DNA_two.count ('G')
C = DNA_two.count ('C')

GC = (DNA_two.count('G') + DNA_two.count('C')) / len(DNA_two)

print(DNA_two.count ('A'))
print(DNA_two.count ('T'))
print(DNA_two.count ('G'))
print(DNA_two.count ('C'))
print((DNA_two.count('G') + DNA_two.count('C')) / len(DNA_two))



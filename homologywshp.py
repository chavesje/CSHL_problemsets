#!/usr/bin/env python3

Sequence1= 'agtctgtca'
Sequence2= 'gatctctgc'
score = 0


for pos in range(0,len(Sequence1)):
	if Sequence1[pos] == Sequence2[pos]:
		score  += 1
		print(score)
	else:
		score -= 1
		print(score)

print("final score", score)

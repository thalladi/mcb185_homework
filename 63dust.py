# Varsha Thalladi
# 63dust.py
# Anisha, Avantika

import sys
import math
import mcb185

fas = sys.argv[1]
w = int(sys.argv[2])
ent = float(sys.argv[3])


def entropy(seq):
	hval = 0.0
	total = len(seq)
	a = seq.count('A') / total
	c = seq.count('C') / total
	g = seq.count('G') / total
	t = seq.count('T') / total

	for base in [a, c, g, t]:
		if base != 0:
			hval -= base * math.log2(base)
	return hval

"""
	if a != 0: hval -= a * math.log2(a)
	if c != 0: hval -= c * math.log2(c)
	if g != 0: hval -= g * math.log2(g)
	if t != 0: hval -= t * math.log2(t)
	return hval
"""

for name, seq in mcb185.read_fasta(fas):
	
	seq = seq[:200]
	dust = list(seq)
	
	for i in range(len(seq) - w + 1):
		dna = seq[i:i+w]
		hval = entropy(dna)
		if hval < ent:
			for j in range(i, i + w):
				dust[j] = 'N'
	
	print('>', name, sep='')
	seq = ''.join(dust)
	
	for i in range(0, len(seq), 60):
		print(seq[i:i+60])



"""

# class demo

import mcb185
import sys

k = 3
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	words = defline.split()
	print(words)
	pro = []
	print(defline, seq[:30])
	for i in range(0, len(seq) -k + 1, 3):
		codon = seq[i:i+3]
		pro.append(codon)
		# aa = translate(codon)
		# pro.append(aa)
		print(codon)

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(defline[:30], seq[:40], len(seq))
"""

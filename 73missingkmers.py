# Varsha Thalladi
# 73missingkmers.py
# Anisha, Lisa

import sys
import mcb185
import itertools

def rev_comp(seq):
	comp = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
	rev_comp = ""
	for i in range(len(seq) -1, -1, -1):
		rev_comp += comp[seq[i]]
	return rev_comp

k = 1
found = False

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	while not found:
		kcount = {}
		for strand in [seq, rev_comp(seq)]:
			for i in range(len(strand) -k +1):
				kmer = strand[i:i+k]
				if kmer not in kcount:
					kcount[kmer] = 1
				else:
					kcount[kmer] += 1
		
		all_kmer = []
		for nts in itertools.product('ACGT', repeat=k):
			kmer = ""
			for nt in nts:
				kmer += nt
			all_kmer.append(kmer)
			
		missing = []
		for kmer in all_kmer:
			if kmer not in kcount:
				missing.append(kmer)
		
		if missing:
			for kmer in sorted(missing):
				print(kmer)
			found = True
		else:
			k += 1
			if k > len(seq):
				print("No missing kmers found.")
				break
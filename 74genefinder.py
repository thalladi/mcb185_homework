# Varsha Thalladi
# 74genefinder.py
# Anisha, Lisa

import sys
import mcb185

def find_orf(seq, min_len):
	stops = ['TAA', 'TAG', 'TGA']
	orfs = []
	i = 0
	
	while i < len(seq) - min_len:
		if seq[i:i+3] == 'ATG':
			for j in range(i+3, len(seq), 3):
				if seq[j:j+3] in stops:
					orf_len = j + 3 - i
					
					if orf_len >= min_len:
						orfs.append((i, j+3))
						i = j + 3
						break
			else:
				i += 3
				continue		
		i += 1
	return orfs

def output_gff(orfs, defline, strand):
	for start, end in orfs:
		print(f"{defline}\t.\tCDS\t{start+1}\t{end}\t.\t{strand}\t.\t.")

def rev_comp(seq):
	comp = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
	rev_comp = ""
	for i in range(len(seq) -1, -1, -1):
		rev_comp += comp[seq[i]]
	return rev_comp

fas = sys.argv[1]
min_orf = int(sys.argv[2]) # 300

for defline, seq in mcb185.read_fasta(fas):
	sliced_seq = seq[:10000]
	orfs_forward = find_orf(sliced_seq, min_orf)
	output_gff(orfs_forward, defline, '+')

	rev_seq = rev_comp(sliced_seq)
	rev_orf = find_orf(rev_seq, min_orf)
	output_gff(rev_orf, defline, '-')


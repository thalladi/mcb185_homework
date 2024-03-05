# toolbox.py
# personal library


# transcription function
def transcribe(dna):
	return dna.replace('T', 'U')

# reverse-complement function
def revcomp(dna):
	rc = []
	for nt in dna[::-1]:
		if nt == 'A': rc.append('T')
		elif nt == 'A': rc.append('G')
		elif nt == 'A': rc.append('C')
		elif nt == 'A': rc.append('A')
		else: rc.append('N')
	return ''.join(rc)


# gc composition
def gc_comp(seq):
	return (seq.count('C') + seq.count('G')) / len(seq)


# gc skew function
def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return (g - c) / (g + c)

# amino acid translation function
def translate(dna):
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if codon == 'ATG':
			aas.append('M')
		elif codon in ['TAA', 'TAG', 'TGA']:
			aas.append('*')
		elif codon in ['TTT', 'TTC']:
			aas.append('F')
		elif codon in ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG']:
			aas.append('L')
		elif codon in ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC']:
			aas.append('S')
		elif codon in ['TAT', 'TAC']:
			aas.append('Y')
		elif codon in ['TGT', 'TGC']:
			aas.append('C')
		elif codon in ['TGG']:
			aas.append('W')
		elif codon in ['CCT', 'CCC', 'CCA', 'CCG']:
			aas.append('P')
		elif codon in ['CAT', 'CAC']:
			aas.append('H')
		elif codon in ['CAA', 'CAG']:
			aas.append('Q')
		elif codon in ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG']:
			aas.append('R')
		elif codon in ['ATT', 'ATC', 'ATA']:
			aas.append('I')
		elif codon in ['ACT', 'ACC', 'ACA', 'ACG']:
			aas.append('T')
		elif codon in ['AAT', 'AAC']:
			aas.append('N')
		elif codon in ['AAA', 'AAG']:
			aas.append('K')
		elif codon in ['GTT', 'GTC', 'GTA', 'GTG']:
			aas.append('V')
		elif codon in ['GCT', 'GCC', 'GCA', 'GCG']:
			aas.append('A')
		elif codon in ['GAT', 'GAC']:
			aas.append('D')
		elif codon in ['GAA', 'GAG']:
			aas.append('E')
		elif codon in ['GGT', 'GGC', 'GGA', 'GGG']:
			aas.append('G')
		else:
			aas.append('X')
	return ''.join(aas)

# kyte doolittle values
import sys

def kyte_doolittle(aa):
	if aa == 'A': return 1.8
	if aa == 'R': return -4.5
	if aa == 'N': return -3.5
	if aa == 'D': return -3.5
	if aa == 'C': return 2.5
	if aa == 'Q': return -3.5
	if aa == 'E': return -3.5
	if aa == 'G': return -0.4
	if aa == 'H': return -3.2
	if aa == 'I': return 4.5
	if aa == 'L': return 3.8
	if aa == 'K': return -3.9
	if aa == 'M': return 1.9
	if aa == 'F': return 2.8
	if aa == 'P': return -1.6
	if aa == 'S': return -0.8
	if aa == 'T': return -0.7
	if aa == 'W': return -0.9
	if aa == 'Y': return -1.3
	if aa == 'V': return 4.2
	sys.exit("illegal value")	
	
"""
# translation function
def translate(dna):
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if codon == 'ATG': aas.append('M')
		elif codon == 'TAA': aas.append('*')
		else: aas.append('X')
	return ''.join(aas)


# alternative translation function
def translate(dna):
	codons = ('ATG', 'TAA')
	aminos = 'M*'
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if codon in codons:
			aas.append(aminos[codons.index(codon)])
		else:
			aas.append('X')
	return ''.join(aas)


# canonical form of sliding window algorithm
w = 10
s = 1
for i in range(0, len(seq) -w +1, s):
	subseq = seq[i:i+w]
"""




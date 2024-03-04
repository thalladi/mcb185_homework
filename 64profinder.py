# Varsha Thalladi
# 64profinder.py
# Anisha, Avantika
# python3 ~/Code/MCB185/src/stylint.py PROGRAM NAME


import sys
import mcb185
import toolbox

fas = sys.argv[1]
min_len = int(sys.argv[2])

def find_prot(trans_seq, min_len):
	valid = []
	protein = ''
	start_found = False
	
	for aa in trans_seq:
		if aa == 'M' and not start_found:
			start_found = True
			protein += aa
		elif start_found:
			protein += aa
			if aa == '*':
				if len(protein) >= min_len:
					valid.append(protein)
				protein = ''
				start_found = False
	return valid
	
def sixft(dna, min_len):
	proteins = []
	frames = [dna, toolbox.revcomp(dna)]
	
	for dna_seq in frames:
		for frame in range(3):
			trans_seq = toolbox.translate(dna_seq[frame:])
			proteins += find_prot(trans_seq, min_len)
	return proteins

output = []
for name, seq in mcb185.read_fasta(fas):
	proteins = sixft(seq, min_len)
	for i, protein in enumerate(proteins):
		identifier = f'{name}-prot-{i}'
		output.append((identifier, protein))
		
for identifier, protein in output:
	print(f'>{identifier}')
	for i in range(0, len(protein), 60):
		print(protein[i:i+60])

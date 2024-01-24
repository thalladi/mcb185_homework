# Varsha Thalladi
# 23hydropathy.py

# Write a function that returns the Kyte-Doolittle hydrophobicity value for an amino acid letter. 
# Demonstrate that the function works by calling it multiple times with different letters.

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
	
	
# examples

print(kyte_doolittle('A'))
print(kyte_doolittle('Y'))
print(kyte_doolittle('S'))
print(kyte_doolittle('C'))
print(kyte_doolittle('U'))

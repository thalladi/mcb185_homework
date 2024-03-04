# Varsha Thalladi
# 61skewer.py

import toolbox

seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
w = 10
for i in range(len(seq) -w +1):
	s = seq[i:i+w]
	# print(i, toolbox.gc_comp(s), toolbox.gc_skew(s))
	print(f'{i}\t{toolbox.gc_comp(s):.3f}\t{toolbox.gc_skew(s):.3f}')
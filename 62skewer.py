# Varsha Thalladi
# 62skewer.py
# Anisha, Avantika
# python3 ~/Code/MCB185/src/stylint.py PROGRAM NAME


import toolbox
import sys

seq = sys.argv[1]
w = int(sys.argv[2])

def slider(seq, w):
	w1 = seq[:w]
	new_gc_comp = toolbox.gc_comp(w1)
	new_gc_skew = toolbox.gc_skew(w1)
	
	for i in range(1, len(seq) - w + 1):
		lnt = seq[i - 1]
		rnt = seq[i + w - 1]
		
		if lnt == 'C' or lnt == 'G':
			new_gc_comp -= 1 / w
			new_gc_skew -= 2 / w
			
		if rnt == 'C' or rnt == 'G':
			new_gc_comp += 1 / w
			new_gc_skew += 2 / w
	
	return new_gc_comp, new_gc_skew

new_gc_comp, new_gc_skew = slider(seq, w)	

print(f'gc comp: {new_gc_comp:.3f}')
print(f'gc skew: {new_gc_skew:.3f}')	

# Varsha Thalladi
# 33triples.py

import math
	
for a in range(1, 100):
	for b in range(a, 100):
		c = math.sqrt(a**2 + b**2)
		if c == c // 1:
			print(a, b, c)		
		

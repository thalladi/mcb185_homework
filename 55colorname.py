# Varsha Thalladi
# 55colorname.py
# python3 ~/Code/MCB185/src/stylint.py PROGRAM NAME

import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

		

def diff(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(p-q)
	return d

	
def fcolor(colorfile, R, G, B):
	mini = 765
	closest = ''
	
	
	with open(colorfile) as fp:
		for line in fp:
			words = line.split()
			name = words[0]
			hexcode = words[1]
			rgb =  words[2].split(',')
		
			for i in range(len(rgb)):
				rgb[i] = int(rgb[i])
		
			dist = diff([R, G, B], rgb)
			if dist < mini:
				mini = dist
				closest = name
	
	return closest

print(fcolor(colorfile, R, G, B))

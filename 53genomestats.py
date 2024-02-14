# Varsha Thalladi
# 53genometats.py
# Anisha Patel
# python3 ~/Code/MCB185/stylint.py PROGRAM NAME

import gzip
import sys

gffpath = sys.argv[1]
feature = sys.argv[2]


distance = []

with gzip.open(gffpath, 'rt') as fp:
	for line in fp:
		if line[0] == '#': continue
		words = line.split()
		if words[2] == feature:
		# print(line)
			beg = int(words[3])
			end = int(words[4])
			distance.append(end - beg + 1)

def count(vals):
	count = 0
	for val in vals:
		count += 1
	return count

print(count(distance))


def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini

print(minimum(distance))

def maximum(vals):
	maxi = vals[0]
	for val in vals[1:]:
		if val > maxi: maxi = val
	return maxi

print(maximum(distance))

def mean(vals):
	total = 0
	for val in vals: total += val
	return total / len(vals)
	
print(mean(distance))

def median(vals):
	vals.sort()
	n = len(vals)
	midpt = n // 2
	
	if n % 2 == 0:
		med = (vals[midpt - 1] + vals[midpt]) / 2
	else:
		med = vals[midpt]
	return med
		
print(median(distance))		

def sd(vals):
	amt = count(vals)
	total = 0
	sqd = 0
	
	for val in vals:
		total += val
	
	mean_val = total / amt
	
	for val in vals:
		sqd += (val - mean_val) ** 2
	return (sqd / amt) ** 0.5

print(sd(distance))
	
"""

python3 53genomestats.py ~/Code/MCB185/data/A.thaliana.gff.gz gene
python3 53genomestats.py ~/Code/MCB185/data/A.thaliana.gff.gz exon
python3 53genomestats.py ~/Code/MCB185/data/A.thaliana.gff.gz CDS

python3 53genomestats.py ~/Code/MCB185/data/C.elegans.gff.gz gene
python3 53genomestats.py ~/Code/MCB185/data/C.elegans.gff.gz exon
python3 53genomestats.py ~/Code/MCB185/data/C.elegans.gff.gz CDS

python3 53genomestats.py ~/Code/MCB185/data/D.melanogaster.gff.gz gene
python3 53genomestats.py ~/Code/MCB185/data/D.melanogaster.gff.gz exon
python3 53genomestats.py ~/Code/MCB185/data/D.melanogaster.gff.gz CDS



"""
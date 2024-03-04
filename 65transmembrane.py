# Varsha Thalladi
# 65transmembrane.py
# Avantika, Anisha
# python3 ~/Code/MCB185/src/stylint.py PROGRAM NAME


import sys
import mcb185
import toolbox

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	success = False
	for i in range(0, 30 -8 + 1):
		sp = seq[i:i+8]
		spave = 0.0		
		for i in sp:
			spave += toolbox.kyte_doolittle(i)
			spave = spave / 8		
		if spave >= 2.5 and 'P' not in sp:
			for j in range(31, len(seq) -11 +1):
				region = seq[j:j+11]
				regionave = 0
				for k in region:
					regionave += toolbox.kyte_doolittle(k)
					regionave = regionave / 11
				if regionave >= 2.0 and 'P' not in region:
					success = True
					break
		if success == True:
			print(defline)
			break




"""
#PREVIOUS TRIALS AND ERRORS

import sys
import mcb185
import toolbox

fas = sys.argv[1]
sequences = mcb185.read_fasta(fas)


def kd_values(seq):
	return [toolbox.kyte_doolittle(aa) for aa in seq]

def ave_kd(seq, start, length):
	
	where = seq[start:start+length]
	kd_val = kd_values(where)
	total = 0.0
	for val in kd_val:
		total += val
	
	return total / length if length > 0 else 0.0

def find_tm(sequences):

	tm_prot = []
	for name, seq in sequences:
		for i in range(23):
			if ave_kd(seq, i, 8) >= 2.5 and 'P' not in seq[i:i+8]:
				for j in range(30, len(seq) - 11 + 1):
					if ave_kd(seq, j, 11) >= 2.0 and 'P' not in seq[j:j+11]:
						tm_prot.append(name)
						break
				break
	return tm_prot
	

tm_prot = find_tm(sequences)
for name in tm_prot:
	print(f'>{name}')

print(tm_prot)


import sys
import mcb185
import toolbox

fasfile = sys.argv[1]
file = mcb185.read_fasta(fasfile)

def kd_values(seq):
    return [toolbox.kyte_doolittle[aa] for aa in seq]

def ave_kd(seq, start, end):
    region = seq[start:end]
    kd_val = kd_values(region)
    total = sum(kd_val)
    count = len(kd_val)
    
    if count != 0:
        return total / count
    else:
        return 0.0

def prol(seq, start, end):
    region = seq[start:end]
    return 'P' in region

# tm = transmembrane
def tm(file):
    tmprot = []
    for name, seq in file:
        pep_ave_kd = ave_kd(seq, 0, 30)
        tm_ave_kd = ave_kd(seq, 30, 41)
        
        if pep_ave_kd >= 2.5:
            if not prol(seq, 0, 30):
                if tm_ave_kd >= 2.0 and not prol(seq, 30, 41):
                    tmprot.append((name, seq))
                    
    return tmprot

result = tm(file)
for name, seq in result:
    print(f'>{name}\n{seq}')




import sys
import mcb185
import toolbox

fasfile = sys.argv[1]
file = mcb185.read_fasta(fasfile)

def kd(seq):
	kd_val = []
	for aa in seq:
		kd_val.append(toolbox.kyte_doolittle[aa])	
	return kd_val
	
def ave_kd(seq, start, end):
	region = seq[start:end]
	kd_val = kd(region)
	total = 0
	count = 0
	
	for val in kd_val:
		total += val
		count += 1
	
	if count != 0: return total / count
	else: return 0.0
	
def prol(seq, start, end):
	region = ''.join(seq[start:end])
	return 'P' in region

# tm = transmembrane
def tm(file):
	tmprot = []
	for name, seq in file:
		pep_ave_kd = ave_kd(seq, 0, 30)
		tm_ave_kd = ave_kd(seq, 30, 41)
		
		if pep_ave_kd >= 2.5:
			if prol(seq, 0, 30):
				continue
			elif tm_ave_kd >= 0:
				if prol(seq, 30, 41):
					continue
				else:
					tmprot.append((name, seq))
	return tmprot

result = tm(file)
print(result)
"""

			
		
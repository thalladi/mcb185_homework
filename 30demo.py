
for nt1 in 'ACGT':
    for nt2 in 'ACGT':
        if nt1 == nt2: print(nt1, nt2, '+1')
        else:          print(nt1, nt2, '-1')
        
nts = 'ACGT'
for nt1 in nts:
    for nt2 in nts:
        if nt1 == nt2: print(nt1, nt2, '+1')
        else:          print(nt1, nt2, '-1')
        
limit = 4
for i in range(0, limit):
    for j in range(i + 1, limit):
        print(i+1, j+1)
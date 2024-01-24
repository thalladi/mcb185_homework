# Varsha Thalladi
# 22oligotemp.py
# coauthor: Anisha Patel

# 1. For oligos <= 13 nt, Tm = (A+T)*2 + (G+C)*4
# 2. For longer oligos, Tm = 64.9 + 41*(G+C -16.4) / (A+T+G+C)


def oligo_temp(A, C, G, T):
	oligo_len = (A + C + G + T)
	if oligo_len <= 13:
		melt_temp = (A+T)*2 + (G+C)*4
	if oligo_len > 13:
		melt_temp = 64.9 + 41*(G+C-16.4) / (A+T+G+C)
	return melt_temp
	
# examples
	
print(oligo_temp(1, 2, 3, 4), "degrees")
print(oligo_temp(12, 21, 10, 15), "degrees")

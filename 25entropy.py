# Varsha Thalladi
# 25entropy.py


# Write a function that calculates Shannon entropy for nucleotide counts a, c, g, t. 

import math

def shannon_entropy(A, C, G, T):
	total_nt = (A + C + G + T)
	a_frac = (A / total_nt) 
	c_frac = (C / total_nt) 
	g_frac = (G / total_nt) 
	t_frac = (T / total_nt) 
	
	if A != 0: a_prob = a_frac * math.log2(a_frac)
	if C != 0: c_prob = c_frac * math.log2(c_frac)
	if G != 0: g_prob = g_frac * math.log2(g_frac)
	if T != 0: t_prob = t_frac * math.log2(t_frac)
	
	entropy = -1 * (a_prob + c_prob + g_prob + t_prob)
	
	return entropy
	
print(shannon_entropy(1, 2, 3, 4))	
print(shannon_entropy(5, 12, 13, 25))	
print(shannon_entropy(3, 6, 5, 8))	

	

	
	





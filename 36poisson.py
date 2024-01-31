# Varsha Thalladi
# 36poisson.py

import math

def poisson(n, k):
	probability = (n**k * math.exp(-n)) / math.factorial(k)
	return probability
	
print(poisson(6, 2))
print(poisson(3, 1))
print(poisson(4, 0))
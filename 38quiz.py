# Varsha Thalladi
# coauthors: Anisha, Avantika, Francesca, Lisa



def gregory(iterations):
	estimate_pi = 1
	sign = -1
	
	for i in range(1, iterations):
		denominator = 2 * i + 1
		now_add = 1 / denominator
		estimate_pi += sign * now_add
		sign *= -1
	return estimate_pi
	
print(gregory(5))
print(gregory(10))
print(gregory(15))
print(gregory(20))
print(gregory(50))
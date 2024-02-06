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
	return estimate_pi * 4
"""	
print(gregory(5))
print(gregory(10))
print(gregory(15))
print(gregory(20))
print(gregory(50))
"""


def nilakantha(iterations):
	estimate_pi = 3
	sign = 1
	
	for i in range(1, iterations):
		denominator = 2 * i * (2 * i + 1) * (2 * i + 2)
		now_add = 4 / denominator
		estimate_pi += sign * now_add
		sign *= -1
	return estimate_pi
"""	
print(nilakantha(5))
print(nilakantha(10))
print(nilakantha(15))
print(nilakantha(20))
print(nilakantha(50))
"""

for i in range(1, 100):
	print(nilakantha(i), gregory(i))
# Varsha Thalladi
# 37nilakantha.py

def nilakantha(iterations):
	estimate_pi = 3
	sign = 1
	
	for i in range(1, iterations):
		denominator = 2 * i * (2 * i + 1) * (2 * i + 2)
		now_add = 4 / denominator
		estimate_pi += sign * now_add
		sign *= -1
	return estimate_pi
	
print(nilakantha(5))
print(nilakantha(10))
print(nilakantha(15))
print(nilakantha(20))
print(nilakantha(50))
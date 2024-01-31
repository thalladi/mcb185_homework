# Varsha Thalladi
# 32fibonacci.py


def fibonacci(n):
	n1 = -1
	n2 = 1
	for i in range(n):
		total = n1 + n2
		print(total)
		n1 = n2
		n2 = total
print(fibonacci(9))
	
	
	
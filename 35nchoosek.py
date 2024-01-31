# Varsha Thalladi
# 35nchoosek.py

def factorial(n):
	if n == 0  or n ==1:
		return 1
	else:
		return n * factorial(n-1)
		
def nchoosek(n, k):
	if k < 0 or k > n:
		return 0
	else:
		return factorial(n) // (factorial(k) * factorial(n - k))
				
print(nchoosek(5, 2))
print(nchoosek(7, 4))
print(nchoosek(8, 6))


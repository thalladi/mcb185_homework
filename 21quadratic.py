# Varsha Thalladi
# 21quadratic.py

# Write a function that solves the quadratic formula (ax^2 + bx + c). 
# Demonstrate that it works by using the formula multiple times within the program.

# formula: y = ax^2 +bx + c

import math

def solve_quad_formula(a, b, c):
	# calculate D
	discriminant = math.sqrt(b**2 - 4*a*c)
	
	# solve for roots
	root1 = (-b + discriminant) / (2*a)
	root2 = (-b - discriminant) / (2*a)
	return root1, root2
	
# examples
	
print(solve_quad_formula(1, 8, 7))
print(solve_quad_formula(2, 12, 16))

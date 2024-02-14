# Varsha Thalladi
# 56birthday.py
# Anisha Patel

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
students = int(sys.argv[3])

shared = 0

for trial in range(trials):
	calendar = [0] * days
	for i in range(students):
		birthday = random.randint(0, days - 1)
		if calendar[birthday] == 1:
			shared += 1
			break
		calendar[birthday] += 1
print(shared / trials)



# some outputs were 0.5122, 0.5127
# Varsha Thalladi
# 47deathsaves.py
# coauthor = Anisha Patel

import random

limit = 1000000

revive = 0
died = 0
stable = 0

for i in range(limit):
	success = 0
	failure = 0
	
	while True:
		roll = random.randint(1, 20)
		if roll == 20:
			revive += 1
			break
		elif roll == 1:
			failure += 2
			if failure >= 3:
				died += 1
				break
		elif roll < 10:
			failure += 1
			if failure >= 3:
				died += 3
				break
		else:
			success += 1
			if success >= 3:
				stable += 1
				break

print(f'revived: {revive / limit}')				
print(f'died: {died / limit}')
print(f'stabilized: {stable / limit}')

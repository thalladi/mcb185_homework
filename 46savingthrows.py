# Varsha Thalladi
# 46savingthrows.py
# coauthor = Anisha Patel

import random


def normal_roll(value):
	fail = 0
	success = 0
	for i in range(10000):
		roll = random.randint(1, 20)
		if roll >= value: success += 1
		else: fail += 1
#	print(success)
	print(success / 10000)
#	print(fail)

print(normal_roll(5))
print(normal_roll(10))
print(normal_roll(15))



def advantage_roll(value):
	fail = 0
	success = 0
	for i in range(10000):
		roll1 = random.randint(1, 20)
		roll2 = random.randint(1, 20)
		if roll1 >= value: success += 1
		elif roll2 >= value: success += 1
		else: fail += 1	
	print(success / 10000)

print(advantage_roll(5))
print(advantage_roll(10))
print(advantage_roll(15))



def disadvantage_roll(value):
	fail = 0
	success = 0
	for i in range(10000):
		roll1 = random.randint(1, 20)
		roll2 = random.randint(1, 20)
		if roll1 <= roll2 and roll1 >= value:
			success += 1
		elif roll2 <= roll1 and roll2 >= value:
			success += 1
		else:
			fail += 1
	print(success / 10000)

print(disadvantage_roll(5))
print(disadvantage_roll(10))
print(disadvantage_roll(15))



"""

limit = 10
fail = 0
success = 0

# DC 5, normal
for i in range(limit):
	roll = random.randint(1, 20)
	if roll >= 5: success += 1
	else: fail += 1
print(success)
print(fail)	


# DC 5, advantage
for i in range(limit):
	roll1 = random.randint(1, 20)
	roll2 = random.randint(1, 20)
	if roll1 >= 5: success += 1
	elif roll2 >= 5: success += 1
	else: fail += 1	
print(success)
print(fail)


# DC 5, disadvantage
for i in range(limit):
	roll1 = random.randint(1, 20)
	roll2 = random.randint(1, 20)
	if roll1 <= roll2 and roll1 >= 5:
		success += 1
	elif roll2 <= roll1 and roll2 >= 5:
		success += 1
	else:
		fail += 1
print(success)
print(fail)


# successes and fails are compounding, troubleshoot that


		if roll1 >= 5: success += 1
		elif roll2 >= 5: success += 1
		else: fail += 1	
	
		
		
for i in range(limit):		
	while True:
		roll = random.randint(1, 20)
		if roll >= 10: success += 1
		else: fail += 1
		
		
for i in range(limit):
	while True:
		roll = random.randint(1, 20)
		if roll >= 15: success += 1
		else: fail += 1
		
		
		






for i in range(limit):
	
	while True:
		dc = random.randint(1, 3)
		# 1 = DC of 5, 2 = DC of 10, 3 = DC of 15
		
		if dc == 1:
			roll = random.randint(1, 20)
			if roll >= 5:
				success += 1
			else:
				failure +=1
				break
		
		if dc == 2:
			roll = random.randint(1, 20)
			if roll >= 10:
				success += 1
			else:
				failure += 1
				break
		
		if dc == 3:
			roll = random.randint(1, 20)
			if roll >= 15:
				success += 1
			else:
				failure += 1
				break


	while True:
		aod = random.randint(1, 2)
		
		if aod == 1:
		# advantage
			d1 = random.randint(1, 20)
			d2 = random.randint(1, 20)
			
			
	#		if d1 >= d2: success += 1
	#		else: fail += 1
		
		if aod == 2: 
		# disadvantage
			d1 = random.randint(1, 20)
			d2 = random.randint(1, 20)
	#		if d1 =< d2: sum2 += d1
	#		else: sum2 += d2

"""

# Varsha Thalladi
# 57birthday.py
# Anisha Patel & Lisa

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
students = int(sys.argv[3])

def bday_cal(trials, days, students):
	shared_bday_trials = 0
	for i in range(trials):
		cal = []
		for j in range(days):
			cal.append(0)
		
		for k in range(students):
			bday = random.randint(0, days - 1)
			cal[bday] += 1
			
		shared_bday = False
		for day_count in cal:
			if day_count > 1:
				shared_bday = True
				break
		
		if shared_bday:
			shared_bday_trials += 1
	
	prob = shared_bday_trials / trials
	return prob
	
p = bday_cal(trials, days, students)
print("Bday paradox:", p)
	


"""
shared = 0

for trial in range(trials):
	calendar = []
	for i in range(students):
		bday = random.randint(0, days - 1)
		if bday in calendar:
			shared += 1
			break
		calendar.append(bday)
print(shared / trials)
"""
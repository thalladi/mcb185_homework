# Varsha Thalladi
# 31fizzbuzz.py
  
for numbers in range(1, 101):
	if (numbers%3==0): 
		print("Fizz")  
	elif (numbers%5==0): 
		print("Buzz")
	elif (numbers%3==0 and numbers%5==0): 
		print("FizzBuzz")
	else:
		print (numbers)
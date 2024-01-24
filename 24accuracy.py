# Varsha Thalladi
# 24accuracy.py

# Given values for true positives, false positives, true negatives, and false negatives, write a function that reports the accuracy and F1 score.


#t_pos
#f_pos
#t_neg
#f_neg

	
def accuracy(t_pos, f_pos, t_neg, f_neg):
	return ((t_pos + t_neg)/(t_pos + f_pos + t_neg + f_neg))
	

def fscore(t_pos, f_pos, t_neg, f_neg):
	return ((t_pos)/(t_pos + 0.5*(f_pos + f_neg)))
	
	
def performance(t_pos, f_pos, t_neg, f_neg):
	return accuracy(t_pos, f_pos, t_neg, f_neg), fscore(t_pos, f_pos, t_neg, f_neg)
	
# examples

print(performance(2, 4, 6, 8))
print(performance(3, 5, 8, 10))
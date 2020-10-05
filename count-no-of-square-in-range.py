#CODE 3
# Python program to count squares between a and b 

def CountSquares(n,a, b): 

	cnt = 0 # initialize result 

	# Traverse through all numbers 
	for i in range (a, b + 1): 
		j = 1; 
		while j ** n <= i: 
			if j ** n == i: 
				cnt = cnt + 1
			j = j + 1
		i = i + 1
	return cnt 

# Driver Code 
n=2
a = 49
b = 65
print ("Count of squares is:", CountSquares(n,a, b) )

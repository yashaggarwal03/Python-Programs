# Python3 program to print terms of binomial 
# This code is contributed by Smitha Dinesh Semwal.  

def factorial(n): 

	f = 1
	for i in range(2, n+1): 
		f *= i 
		
	return f 

# Function to print the series 
def series(A, X, n): 
	
	# calculating the value of n! 
	nFact = factorial(n) 

	# loop to display the series 
	for i in range(0, n + 1): 
		
		# For calculating the 
		# value of nCr 
		niFact = factorial(n - i) 
		iFact = factorial(i) 

		# calculating the value of 
		# A to the power k and X to 
		# the power k 
		aPow = pow(A, n - i) 
		xPow = pow(X, i) 

		# display the series 
		print (int((nFact * aPow * xPow) /
				(niFact * iFact)), end = " ") 
	
# Driver Code 
A = 3; X = 4; n = 5
series(A, X, n) 



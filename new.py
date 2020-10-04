if 5>3:
   print("correct")
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()   

x=1
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

import random

print(random.randrange(1, 10))

b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[-5:-2])

# Check if the phrase "ain" is present in the following text:

txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

# Check if the phrase "ain" is NOT present in the following text:

txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x) 


# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

# Example
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

txt = "We are the so-called \"Vikings\" from the north."
print(txt) 

# # CODE 1
# # pyramid pattern 
  
# def printPattern(n) : 
#     k = 0
#     for i in range(1,n) : #row 6 
      
#         # Print spaces 
#         for j in range(i,n-1) : 
#             print(' ', end='') 
          
#         # Print # 
#         while (k != (2 * i - 1)) : 
#             if (k == 0 or k == 2 * i - 2) : 
#                 print('*', end='') 
#             else : 
#                 print(' ', end ='') 
#             k = k + 1
#         k = 0; 
#         print ("") # print next row 
          
#     # print last row 
#     for i in range(0, 2 * n -3) : 
#         print ('*', end = '') 
  
# # Driver code  
# n = 10
# printPattern(n) 
  
# print("\n")
  #CODE 2
  # Returns sum of n + nn + nnn + .... (m times) 
# def Series(n): 

# 	# Converting the number to string 
# 	str_n = str(n) 

# 	# Initializing result as number and string 
# 	sums = n 
# 	sum_str = str(n) 

# 	# Adding remaining terms 
# 	for i in range(1, n): 
		
# 		# Concatenating the string making n, nn, nnn... 
# 		sum_str = sum_str + str_n 
		
# 		# Before adding converting back to integer 
# 		sums = sums + int(sum_str) 

# 	return sums 

# # Driver Code 
# n = 2
# total = Series(n) 
# print(total) 


# #CODE 3
# # Python program to count squares between a and b 

# def CountSquares(n,a, b): 

# 	cnt = 0 # initialize result 

# 	# Traverse through all numbers 
# 	for i in range (a, b + 1): 
# 		j = 1; 
# 		while j ** n <= i: 
# 			if j ** n == i: 
# 				cnt = cnt + 1
# 			j = j + 1
# 		i = i + 1
# 	return cnt 

# # Driver Code 
# n=2
# a = 49
# b = 65
# print ("Count of squares is:", CountSquares(n,a, b) )

#CODE 4

def checkPattern(string, pattern): 

	# len stores length of the given pattern 
	l = len(pattern) 

	# if length of pattern is more than length 
	# of input string, return false; 
	if len(string) < l: 
		return False

	for i in range(l - 1): 

		# x, y are two adjacent characters in pattern 
		x = pattern[i] 
		y = pattern[i + 1] 

		# find index of last occurrence of 
		# character x in the input string 
		last = string.rindex(x) 

		# find index of first occurrence of 
		# character y in the input string 
		first = string.index(y) 

		# return false if x or y are not present 
		# in the input string OR last occurrence of 
		# x is after the first occurrence of y 
		# in the input string 
		if last == -1 or first == -1 or last > first: 
			return False

	# return true if 
	# string matches the pattern 
	return True

# Driver Code 
string = "a rabbit jumps joyfully"
first="a"
second="j"
pattern = first + second
print(checkPattern(string, pattern)) 

#CODE 5

# import datetime

# def is_date_the_nth_friday_of_month(nth, date=None):
#     #nth is an integer representing the nth weekday of the month
#     #date is a datetime.datetime object, which you can create by doing datetime.datetime(2016,1,11) for January 11th, 2016

#     if not date:
#         #if date is None, then use today as the date
#         date = datetime.datetime.today()

#     if date.weekday() == 4:
#         #if the weekday of date is Friday, then see if it is the nth Friday
#         if (date.day - 1) // 7 == (nth - 1):
#             #We use integer division to determine the nth Friday
#             #if this integer division == 0, then date is the first Friday, 
#             # if the integer division is...
#             #   1 == 2nd Friday
#             #   2 == 3rd Friday
#             #   3 == 4th Friday
#             #   4 == 5th Friday
#             return True

#     return False
# date=2,2020
# is_date_the_nth_friday_of_month(12, date)
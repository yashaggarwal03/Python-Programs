# Find Sum of Geometric Progression Series
import math

FirstNum = int(input("Please Enter First Number of an G.P. : : "))
tn = int(input("Please Enter the Total Numbers in this G.P. : : "))
comRatio = int(input("Please Enter the Common Ratio : "))

total = (FirstNum * (1 - math.pow(comRatio, tn ))) / (1- comRatio)
nth = FirstNum * (math.pow(comRatio, tn - 1))

print("The Sum of G.P. : " , total)
print("The nth Term of G.P. : " , nth)


""""
Please Enter First Number of an G.P. : : 
2
Please Enter the Total Numbers in this G.P. : : 
7
Please Enter the Common Ratio : 
3
The Sum of G.P. :  2186.0
The nth Term of G.P. :  1458.0
"""

#  Input = Integer n
# Boolean = True or False
# if true          if False
# *                *****
# **               ****
# ***              **
# *                *

print("This is Program for Pattern Printing")
row = int(input("How many line You wish to print"))
pattern = int(input("Input 1 for Asending and 0 for Desending"))
if pattern <= 1:
    n = bool(pattern)
    print(pattern)
    if n == True:
        for i in range(1,row+1):
            print("\n",end=" ")
            for j in range(1,i+1):
                print("*",end=" ")

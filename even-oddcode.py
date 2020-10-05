#even-odd finding in a list in python

list=[23,4,5,6,78,90,33]

even=[]
odd=[]

for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print(min(even))        
print(max(odd))

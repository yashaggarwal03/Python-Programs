#
num = int(input("Enter a number: "))

temp = num
while temp > 0:
   digit = temp %.10
   sum += digit ** 3
   temp //= 10
 
 if num == sum:
  print(num,"is an Appolo number")
else:
  print(num,"is not Appolo number")
    

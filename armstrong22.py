# https://www.facebook.com/100012984916915/posts/1035265666916254/
# Subscribed By Code House
num = int(input("Enter a number: "))

sum=0

temp = num
while temp>0:
  digit = temp % 10
  sum += digit ** 3
  temp //=10
  
if num == sum:
   print(num,"is an armstrong number")
else:
   print(num,"is not an armstrong number")

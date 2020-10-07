#https://www.facebook.com/varun.kansal.50364/posts/108267661047265
# subscribed by evil is devil
Num=int(input())
i=1
sum=0
sum1=0
d=(len(str(Num)))
n=Num
while i<=d:
    l=n%10
    n=n//10
    if l%2==0:
        
        sum=sum+l
    
    else:
        
        sum1=sum1+l
        
    i=i+1
    
        
print (sum ,sum1)

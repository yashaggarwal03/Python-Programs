'''
Created By Shouvik Dutta.

This Question was asked in Google Summer Online Coding Challenge.

A number n is given to you and you have to divide the nuber in two numbers say x,y.
Such that:
        x+y=n
        and x,y does not contain digit 7.
You have to answer for T different test cases.
cnostraint:
    1<=n<=10^7
    1<=T<=10^5
 '''
 
 #Code
 T=int(input())
for _ in range(T):
    k=int(input())
    a,b=[],[]
    while k:
        x=k%10
        if x==7:
            a.append(6)
            b.append(1)
        else:
            a.append(x)
            b.append(0)
        k//=10
    num1,num2=0,0
    lim=len(a)
    for i in range(lim-1,-1,-1):
        num1=num1*10+a[i]
        num2=num2*10+b[i]
    print(num1,num2)

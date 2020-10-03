# https://www.facebook.com/jasmeet.singh.77920/posts/3180807528714187
# Subscribed by Code House

def Fibonacci(n):
    if n<=0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
 
print(Fibonacci(9))

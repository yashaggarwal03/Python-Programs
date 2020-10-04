# https://www.facebook.com/ratnesh.tiwar.3/posts/2792522061026004
# subscribed by ratnesh tiwari
def isPrime(n): 
    if (n <= 1): 
        return False1 
    for i in range(2, n//2): 
        if (n % i == 0): 
            return False
  
    return True
if isPrime(11): 
    print ("true") 
else: 
    print ("false") 

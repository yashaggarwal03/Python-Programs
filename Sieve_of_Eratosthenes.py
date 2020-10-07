#https://m.facebook.com/story.php?story_fbid=2848722018739963&id=100008065788593
#subscribed by Sam Parker

import math

n = 200 # n is any arbitrary integer
List = []

for x in xrange(2, n): # add numbers from 2 to n - 1 to List
    List.append(x)
# note the above statement is equivalent to List = range(2, n)

p = 2 # p is a prime

while not int(math.sqrt(p)) + 1 > n: # continue to mark out primes until square root of p is less than n

    for x in xrange(p * 2, n, p): # remove all the multiples of p
        List[x - 2] = 0

    p += 1

    while p - 2 < len(List) and List[p - 2] == 0: # assign p to the next prime. Next prime is the next non zero number in the list
        p += 1

for x in List: # search for non zero or prime numbers in the list and print them
    if x != 0:
        print x

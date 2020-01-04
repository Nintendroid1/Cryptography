import sys, math

# https://www.geeksforgeeks.org/segmented-sieve-print-primes-in-a-range/
# This functions finds all primes smaller than limit  
# using simple sieve of eratosthenes.  It stores found  
# primes in list prime[]  
def simpleSieve(limit, primes): 
    mark = [False]*(limit+1) 
      
    for i in range(2, limit+1): 
        if not mark[i]: 
            # If not marked yet, then its a prime 
            primes.append(i) 
            for j in range(i, limit+1, i): 
                mark[j] = True
  
  
# Finds all prime numbers in given range using  
# segmented sieve 
def primesInRange(low, high): 
      
    # Comput all primes smaller or equal to  
    # square root of high using simple sieve  
    limit = math.floor(math.sqrt(high)) + 1
    primes = list() 
    simpleSieve(limit, primes) 
  
    # Count of elements in given range  
    n = high - low + 1
      
    # Declaring boolean only for [low, high] 
    mark = [False]*(n+1) 
  
    # Use the found primes by simpleSieve() to find  
    # primes in given range 
    for i in range(len(primes)): 
        # Find the minimum number in [low..high] that is  
        # a multiple of prime[i] (divisible by prime[i])  
        loLim = math.floor(low/primes[i]) * primes[i] 
        if loLim < low: 
            loLim += primes[i] 
        if loLim == primes[i]: 
            loLim += primes[i] 
  
        # Mark multiples of primes[i] in [low..high]:   
        # We are marking j - low for j, i.e. each number   
        # in range [low, high] is mapped to [0, high-low]   
        # so if range is [50, 100] marking 50 corresponds   
        # to marking 0, marking 51 corresponds to 1 and   
        # so on. In this way we need to allocate space   
        # only for range  
        for j in range(loLim, high+1, primes[i]): 
            mark[j-low] = True
  
    # Numbers which are not marked in range, are prime   
    for i in range(low, high+1): 
        if not mark[i-low]: 
            print(i, end = " ")  

if __name__=="__main__":
    if(len(sys.argv) == 3):
        low = int(sys.argv[1])
        high = int(sys.argv[2])
        primesInRange(low, high)
        # limit = 600851475143
        # increment = int(math.ceil(math.sqrt(limit)))
        # for i in range(0, limit, increment):
        #     low = i
        #     high = min(i+increment, limit)
        #     primesInRange(low, high)
    else:
        print("Input a min and max generate primes from min and max")
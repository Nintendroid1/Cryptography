import sys, math, random

allPrimes = []

# Python program to print all primes smaller than or equal to 
# n using Sieve of Eratosthenes 
def SieveOfEratosthenes(n): 
	# Create a boolean array "prime[0..n]" and initialize 
	# all entries it as true. A value in prime[i] will 
	# finally be false if i is Not a prime, else true. 
	prime = [True for i in range(n+1)] 
	p = 2
	while (p * p <= n): 
		
		# If prime[p] is not changed, then it is a prime 
		if (prime[p] == True): 
			
			# Update all multiples of p 
			for i in range(p * p, n+1, p): 
				prime[i] = False
		p += 1
	
	# Print all prime numbers 
	for p in range(2, n): 
		if prime[p]: allPrimes.append(p) 

if __name__=="__main__":
    if(len(sys.argv) == 3):
        n = int(sys.argv[1])
        k = int(sys.argv[2])

        #Generate factor base of 1st k primes
        SieveOfEratosthenes(1000)
        factorBase = allPrimes[:k]
        
        for x in factorBase:
            print(x)
        x = int(random.randrange(1, n))

    else:
        print("Input an n to factor and k to generate k primes for factor base B")
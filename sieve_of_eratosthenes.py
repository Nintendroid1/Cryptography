import sys, math

#https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def sieve_of_eratosthenes(limit):
    ceil_sqrt_limit = int(math.ceil(math.sqrt(limit)))
    vals = [True] * limit
    for i in range(2, ceil_sqrt_limit):
        if vals[i]:
            for j in range(pow(i,2), len(vals), i):
                vals[j] = False
    
    primes = []
    for k in range(len(vals)):
        if vals[k]:
            primes.append(k)
            
    print(primes[2:])

if __name__=="__main__":
    if(len(sys.argv) == 2):
        sieve_of_eratosthenes(int(sys.argv[1]))
    else:
        print("Input a limit n to generate primes from 2 to n")
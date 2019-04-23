import operator as op
from functools import reduce
import math

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

# Function to check 
# Log base 2 
def Log2(x): 
    return (math.log10(x)/math.log10(2)); 
  
# Function to check 
# if x is power of 2 
def isPowerOfTwo(n): 
    return (math.ceil(Log2(n))==math.floor(Log2(n)));  

def multiple2(n):
    i=0
    result = 1+i+ncr(i,2)
    while(not isPowerOfTwo(result) or i < n):
        i+=1
        result = 1+i+ncr(i,2)
    print("n=%d, result=%d" %(i,result))

multiple2(20)
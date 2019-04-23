"""Sphere Packing Code"""

import operator as op
from functools import reduce
import math

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

def sumChoose(n, t):
    denominator = 1
    for j in range(t+1):
        denominator += ncr(n, j)
    return denominator

#n=Length of codeword t=number of errors to correct
def minLength(n, t):
    i = n
    numerator = 2**i
    denominator = (sumChoose(i, t))
    result = numerator/denominator
    while(2**n > result):
        i += 1
        numerator = 2**i
        denominator = (sumChoose(i, t))
        result = numerator/denominator
        
    print("Result:%d\n"%(result))
    print("n=%d, numerator=%d, denominator=%d" %(i, numerator, denominator))

minLength(20, 1)   
minLength(20, 2)   
"""
	MATH 4175 - HW 2
	Valid Keys in mod n for an Affine Cipher
	Nathaniel Salazar
"""

import sys

#Helper method to find the gcd using Euclidean Algorithm
def gcd(x: int, y: int) -> int:
    while(y):
        x, y = y, x%y
        
    return x

if __name__== "__main__":
    if(len(sys.argv) == 2):
        n=int(sys.argv[1])
    else:
        print("Please input a the size of n");
    count = 0;
    beta = n #No restriction on beta
    for i in range(n):
        print("gcd("+str(i)+","+str(n)+")="+str(gcd(i, n)))
        if(gcd(i, n) == 1):
            count += 1
    count *= beta
    print("There are " + str(count) + " valid affine keys in mod "+ str(n))
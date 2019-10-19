import sys, math, random

def reverse(s): 
    str = "" 
    for i in s: 
        str = i + str
    return str

def factor_rsa(n, e, d):
    #a = int(random.randrange(2, n))
    # a = 286413805994
    a = 279237114177

    y = math.gcd(a, n)
    if(y != 1): 
        print("%d=%d*%d" %(n,y, n//y))
        return True

    #ed-1=2^k*m
    val = int((e*d)-1)
    k = 0
    binaryRep = '{0:08b}'.format(val)
    revBinaryRep = reverse(binaryRep)
    for x in revBinaryRep:
        if(x != '0'):
            break
        else:
            k = k + 1

    m = int((val)//pow(2,k))

    a = pow(a, m, n) #a=a^m mod n

    if((a % n) == 1 or (a % n) == n-1): return False
    
    a_0 = 0
    while((a%n) != 1):
        a_0 = a
        a = pow(a,2,n)

    if((a_0 % n) == n-1): return False
    else:
        y = math.gcd(a_0-1, n)
        print("%d=%d*%d" %(n,y, n//y))
        return True

if __name__=="__main__":
    if(len(sys.argv) == 4):
        n = int(sys.argv[1])
        e = int(sys.argv[2])
        d = int(sys.argv[3])
        #print("n=%d e=%d d=%d" %(n,e,d))
        
        if(not factor_rsa(n,e,d)):
            print("No factor found for %d" %(n))
    else:
        print("Input n to be factored and encryption (e) and decryption (d) exponent")
        
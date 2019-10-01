import sys
import random

def reverse(s): 
    str = "" 
    for i in s: 
        str = i + str
    return str

def miller_rabin(n):
    if(n<3):
        print("Too small, try again")
        return True
    if(n%2 == 0):
        return True
    a = int(random.randrange(2, n))

    k = 0
    binaryRep = '{0:08b}'.format(n-1)
    revBinaryRep = reverse(binaryRep)
    for x in revBinaryRep:
        if(x != '0'):
            break
        else:
            k = k + 1

    m = int((n-1)//pow(2,k))

    b = pow(a, m, n) #b=a^m mod n

    if((b % n) == 1): 
        return False
    
    for i in range(k):
        if((b % n) == n-1):
            return False

        b = pow(b,2,n) #b=b^2 mod n
    return True

def extensive_miller_rabin(n):
    for i in range(100):
        if(miller_rabin(n)):
            return True
    return False


if __name__=="__main__":
    #Generate integer with 150 decimal digits
    p = int(random.randrange(pow(10,149), pow(10,150)))

    #Ensure integer is odd and passes Miller-Rabin test
    while(extensive_miller_rabin(p)):
        p = int(random.randrange(pow(10,149), pow(10,150)))
        #print(p)
        
    print("Final p:")
    print(p)    

    q = int(random.randrange(pow(10,149),  pow(10,150)))

    while((q%2)==0 or extensive_miller_rabin(q)):
        q = int(random.randrange(pow(10,149),  pow(10,150)))
        #print(q)

    print("Final q:")
    print(q)
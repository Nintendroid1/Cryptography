import sys, math, random

def reverse(s): 
    str = "" 
    for i in s: 
        str = i + str
    return str

def miller_rabin(n):
    if(n<3):
        #print("Too small, try again")
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
    if(len(sys.argv) == 2):
        n = int(sys.argv[1])
        
        factorBase = [-1,2,3,5,7,11,13,17,19,23,29,31]

        overallFactors = [0] * len(factorBase)
        eligibleBases = []
        a=500
        finalX = 1
        finalY = 1
        while(math.gcd(finalX-finalY,n) == 1 or math.gcd(finalX-finalY,n) == n):
            factors = [0] * len(factorBase)
            
            x = 0
            y=1
            z = math.gcd(x-y,n)
            x = pow(a,2, n)
            #print(str(a) + "^2=" + str(x))            
            x_0 = x

            neg_x = (-1*x) % n
            #If negative is close to 0 and is not prime
            if(neg_x < n//2 and extensive_miller_rabin(neg_x)):
                x_0 = neg_x
                factors[0] += 1 #Increment powers

            for i in range(1,len(factorBase)):
                #Find factors in terms of the factor base
                while(x_0 % factorBase[i] == 0):
                    x_0 = x_0//factorBase[i]
                    
                    if(x_0 == 0):break

                    factors[i] += 1 #Increment powers
                
            #Can factor over factor base
            if(x_0 == 1 and factors != [0] * len(factorBase)):
                eligibleBases.append(a)
                #print(str(a) + "^2=" + str(x) + " " + str(factors))
                # result = ""

                for i in range(len(factorBase)):
                    # if(factors[i] != 0):
                    #     result += str(factorBase[i]) +"^" + str(factors[i])
                    #     result += " * "
                
                    overallFactors[i] += factors[i]
                #print(result)
                #print("\n")   
            a += 1

            #Find relationship
            finalX = 1
            for i in range(len(eligibleBases)):
                finalX *= eligibleBases[i]
            finalX = pow(finalX,2,n)

            finalY = 1
            for i in range(len(overallFactors)):
                finalY *= pow(factorBase[i], overallFactors[i], n)
            finalY = pow(finalY,2,n)

        print(eligibleBases)
        print(overallFactors)
        print(finalX)
        print(finalY)
        print(math.gcd(finalX-finalY,n))
    
    else:
        print("Input an n to factor")
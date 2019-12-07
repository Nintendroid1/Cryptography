import sys, math

if __name__=="__main__":
    print(len(sys.argv))
    if(len(sys.argv) == 2):
        m = int(sys.argv[1])
        print(m)

        #phi_m = phi(m)
        phi_m = m-1
        
        #Prime factorization
        temp = phi_m
        factorBase = [2,3,5,7,11,13,17,19,23,29,31] #Can be expanded
        factors = [0] * len(factorBase)

        for i in range(len(factorBase)):
                #Find factors in terms of the factor base
                while(temp % factorBase[i] == 0):
                    temp = temp//factorBase[i]
                    
                    if(temp == 0):break

                    factors[i] += 1 #Increment powers
                    print("Here")
        print(factors)
    else:
        print("Please input m to prime factorize")
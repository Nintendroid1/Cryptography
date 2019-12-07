import sys, math

if __name__=="__main__":
    if(len(sys.argv) == 2):
        m = int(sys.argv[1])
        
        #Prime factorization
        temp = m
        factorBase = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97] #Can be expanded
        factors = [0] * len(factorBase)

        for i in range(len(factorBase)):
                #Find factors in terms of the factor base
                while(temp % factorBase[i] == 0):
                    temp = temp//factorBase[i]
                    
                    if(temp == 0):break

                    factors[i] += 1 #Increment powers
        print(factors)
    else:
        print("Please input m to prime factorize")
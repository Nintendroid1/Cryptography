import sys, math

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

if __name__=="__main__":
    if(len(sys.argv) == 4 or len(sys.argv) == 5):
        verbose = False
        if(sys.argv[1] == "-v"):
            verbose = True
            alpha = int(sys.argv[2])
            beta = int(sys.argv[3])
            m = int(sys.argv[4])
        else:
            alpha = int(sys.argv[1])
            beta = int(sys.argv[2])
            m = int(sys.argv[3])

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
        if(verbose):
        	print(factors)

        #Iterate through
        for index in range(len(factorBase)):
        	if(factors[index] == 0):continue

        	maxExponent = factors[index]
        	q = factorBase[index]
        	beta_i = beta
        	x = 0
        	coeff = 1
        	for i in range(1, maxExponent+1):
        		left_exp = phi_m//pow(q,i)
        		left = pow(beta_i, left_exp, m)

        		right_exp = phi_m//q
        		right = pow(alpha, right_exp, m)

        		x_i = 0
        		#beta_i^((p-1)/q^i+1) \equiv (alpha^((p-1)/q))^x_i
        		while(left != pow(right, x_i, m)):
        			x_i += 1

        		if(verbose):
        			print(str(q) + "^" + str(i))
        			print(str(left) + "=" + str(right) + "^" + str(x_i))
        			print(str(coeff) + "x_" + str(i) + "\n")

        		x += coeff*x_i
        		coeff *= q

        		neg_x_i = pow(modinv(x_i),x_i, m)
        		print(pow(modinv()))

        		#beta_i+1 \equiv beta_i*alpha^(-x_i*q^i) mod m
        		beta_i = pow(beta_i, alpha)





    else:
        print("Please input alpha, beta, and m, to calculate log_alpha(beta) mod m")
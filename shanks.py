import sys, math

def phi(n) : 
  
    result = n   # Initialize result as n 
       
    # Consider all prime factors 
    # of n and for every prime 
    # factor p, multiply result with (1 - 1 / p) 
    p = 2
    while(p * p<= n) : 
  
        # Check if p is a prime factor. 
        if (n % p == 0) : 
  
            # If yes, then update n and result 
            while (n % p == 0) : 
                n = n // p 
            result = result * (1.0 - (1.0 / (float) (p))) 
        p = p + 1
          
          
    # If n has a prime factor 
    # greater than sqrt(n) 
    # (There can be at-most one 
    # such prime factor) 
    if (n > 1) : 
        result = result * (1.0 - (1.0 / (float)(n))) 
   
    return (int)(result) 

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

        phi_m = phi(m)
        m_0 = math.ceil(math.sqrt(phi_m))
        
        if(verbose):
            print("phi_m=" +str(phi_m))
            print("m=" + str(m_0))

        L1 = []
        L2 = []

        for i in range(m_0):
            #(i, alpha^(m_0*i)) mod m
            L1.append(pow(alpha, m_0*i, m))
        if(verbose):
            print("L1=" +str(L1) + "\n")

        #alpha^-1
        alpha_inverse = pow(alpha,phi_m-1, m)
        if(verbose):
            print("alpha_inverse=" +str(alpha_inverse))

        for j in range(m_0):
            #(j, beta*alpha^-j) mod m
            L2.append(beta*pow(alpha_inverse, j, m)%m)
        
        if(verbose):
            print("L2=" +str(L2) + "\n")

        for i in range(len(L1)):
            for j in range(len(L2)):
                if(L1[i]==L2[j]):#set(L1)&set(L2)
                    if(verbose):
                        print("i=" +str(i) + ", j=" + str(j))
                    
                    #k = alpha^(i*m)*alpha^(j) = beta
                    k = (i*m_0)+j
                    if(verbose):
                        print("k=" +str(i)+"*"+str(m_0)+"+"+str(j))
                    print("log_" + str(alpha)+"(" + str(beta )+ ")=" + str(k) + " mod m")
                    sys.exit()
    else:
        print("Please input alpha, beta, and m, to calculate log_alpha(beta) mod m")
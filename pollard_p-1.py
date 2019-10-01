import sys, math

if __name__=="__main__":
    if(len(sys.argv) == 3):
        n = int(sys.argv[1])
        a = 2
        B = int(sys.argv[2])

        for i in range(2,B+1):
            a = pow(a,i, n) #a=a^i (mod n)
            d = int(math.gcd(a - 1, n))

            print("i=%d a=%d d=%d"%(i,a,d))

            if(d > 1 and d < n):
                d_2 = n // d
                print("Factors are %d and %d" % (d, d_2))
                sys.exit()

        print("Factor is not found, input a different B")
    else:
        print("Please input n to be factored using Pollard p-1 algorithm and B for a bound")
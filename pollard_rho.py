import sys, math

#Function used for pollard rho algorithm
def fun(x):
    return pow(x,2) + 1

if __name__=="__main__":
    if(len(sys.argv) == 2):
        n = int(sys.argv[1])
        x = 1
        y = 1
        p = 1

        i = 0
        while(p==1):
            x = fun(x) % n
            y = fun(fun(y)) % n

            p = math.gcd(y-x, n)

            #print("i=%d x=%d y=%d p=%d" %(i,x,y,p))
            i = i+1

        if(p==n):
            print("\nn could not be factored")
        else:
            q = n // p
            print("\nAfter %d iterations:"%(i))
            print("p=%d q=%d" % (p, q))

    else:
        print("Please input n to be factored using Pollard rho algorithm")
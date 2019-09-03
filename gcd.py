import sys

if __name__=="__main__":
    if(len(sys.argv) == 3):
        a = int(sys.argv[1])
        b = int(sys.argv[2])

        large = a
        small = b

        if(a < b):
            large = b
            small = a
        
        #Keep dividing until remainder is 0
        remainder = large % small
        factor = 1
        while(remainder != 0):
            remainder = large % small
            factor = (large - remainder) / small
            print("%d = %d*%d + %d" %(large, factor, small, remainder))

            #Reset for next iteration
            large = small
            small = remainder

        print("d=%d" %(large))
    else:
        print("Please input a 2 integers to find the gcd")
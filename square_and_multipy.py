import sys

if __name__=="__main__":
    if(len(sys.argv) == 4):
        b = int(sys.argv[1])
        e = int(sys.argv[2])
        m = int(sys.argv[3])

        binaryRep = '{0:08b}'.format(e)

        print("Base=%d, Exponent=%d, Modulus=%d" %(b,e,m))
        print("Binary Representation of Exponent: %s" %(binaryRep))

        result = 1 # b^0
        for x in binaryRep:
            foo = str(x)
            result = pow(result, 2, m) #square
            foo += " => " + str(result)

            if(x=='1'):
                result = (result*b) % m # multiply
                foo += " => " + str(result)

            print(foo)
        print("%d=%d^%d (mod %d)" % (result, b, e, m))

    else:
        print("Please type, base(b), exponent(e), and mod(m)")
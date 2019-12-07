import sys

if __name__=="__main__":
    if(len(sys.argv) == 3):
        a = int(sys.argv[1])
        n = int(sys.argv[2])

        print(str(a) + "/" + str(n))
        
        originalA = a
        originalN = n
        a = a % n
        result = 1
        while(a != 0):
            while(a % 2 == 0):
                a /= 2
                r = n % 8
                if(n % 8 == 3 or n % 8 == 5):
                    result *= -1
                print(str(a) + "/" + str(n))
            temp = a
            a = n 
            n = temp
            
            if(a % 4 == 3 and n % 4 == 3):
                result *= -1

            a = a % n
            print(str(a) + "/" + str(n))

        if (n == 1):
            answer = ""
            if(result == 1):
                answer = "QR"
            else:
                answer = "QNR"
            print("Result= " + str(result) + " Therefore " +str(originalA) + " is a " + answer + " mod " + str(originalN))
        else:
            print("Result= 0 Therefore " + str(originalN) + "|" + str(originalA))

    else:
        print("Please input a and n to determine if a is a QR or QNR")
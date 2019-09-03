import sys

if __name__=="__main__":
    if(len(sys.argv) == 2):
        val = sys.argv[1].lower() #String to convert
        adj = 97 #Shift the ascii val

        total = 0
        total = total + ord(val[0])-adj

        res = ''
        res+= str(ord(val[1][0])-adj)

        i = 1
        while(i != len(val)):
            total = total + ord(val[i])-adj

            res+='+'
            res+= str(ord(val[i])-adj)
            i+= 1

        res += ' = ' + str(total)
        print(res)
    else:
        print("Please input a string")

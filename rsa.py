import sys
def decode(x,length):
    digits = []
    word = ''
    for i in range(length):
        digits.append(x % 26)
        x = x // 26
    while(digits):
        word += chr(ord('a')+digits.pop())
    return word
    
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
    if(len(sys.argv) == 4):
        n = int(sys.argv[1])
        e = int(sys.argv[2])
        
        d = modinv(e, phi(n)) #d\equiv e^-1 mod phi(n)

        f = open(sys.argv[3], "r")
        if f.mode == "r":
            results = f.read()
            resultList = results.split()
            final = ""

            for ciphertext in resultList:
                decryption = pow(int(ciphertext), d, n) #\gamma^d mod n
                plaintext = decode(decryption, 3) # Assume 3-letter length
                print("%s => %d => %s" %(ciphertext, decryption, plaintext))

                final+=plaintext
            print(final)
        else:
            print("Invalid File")

    else:
        print("Please type, n, e, and a file to decrypt in RSA")
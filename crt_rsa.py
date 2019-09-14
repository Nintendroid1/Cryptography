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

if __name__=="__main__":
    if(len(sys.argv) == 5):
        p = int(sys.argv[1])
        q = int(sys.argv[2])
        d = int(sys.argv[3])
        y = int(sys.argv[4])
        n = p*q

        d_p = d % (p-1) #d mod(p-1)
        d_q = d % (q-1) #d mod(q-1)

        M_p = modinv(q, p) #q^-1 mod p
        M_q = modinv(p, q) #p^-1 mod q

        x_p = pow(y, d_p, p) #y^d_p mod p
        x_q = pow(y, d_q, q) #y_d_q mod q
        x = ((M_p * q * x_p) + (M_q * p * x_q)) % n # M_p*q*x_p + M_q*p*x_q mod n

        print("p=%d, q=%d, d=%d, y=%d, n=%d\nd_p=%d, d_q=%d\nM_p=%d, M_q=%d\nx_p=%d, x_q=%d, x=%d" % (p,q,d,y,n,d_p,d_q,M_p,M_q,x_p,x_q,x))
        print(decode(x, 5))

    else:
        print("Please type, p, q, d, and y to decrypt in RSA using CRT")
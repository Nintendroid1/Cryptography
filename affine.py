import sys

#Encrypts a string using an alphine cipher
def affineEncrypt(plaintext: str, alpha: int, beta: int) -> str:
    plaintext = plaintext.lower()
    ciphertext = []
    for p in plaintext:
        n = ord(p) - 97 #a=97 in ascii, ord converts to ascii
        n = (alpha*n +beta) % 26
        ciphertext.append(chr(n+97).upper()) #chr converts to char
    return ''.join(ciphertext)

#Helper method to find the inverse for alpha in mod 26
def alphaInverse(alpha: int) -> int:
    count = 0
    while((alpha*count)%26 !=1 or count < 26):
        count += 1
    return count

#Helper method to find the gcd using Euclidean Algorithm
def gcd(x: int, y: int) -> int:
    while(y):
        x, y = y, x%y
        
    return x
    
#Decrypts a string that was encrypted by an alphine cipher    
def affineDecrypt(ciphertext: str, alpha: int, beta: int) -> str:
    #Ensure alpha is valid
    if(gcd(alpha, 26)!=1):return 'Not valid alpha'
    
    ciphertext = ciphertext.upper()
    plaintext = []
    for c in ciphertext:
        n = ord(c) - 65 #A=65 in ascii
        n = (alphaInverse(alpha)*(n-beta)) % 26
        plaintext.append(chr(n+65).lower())
    return ''.join(plaintext)


def main():
    if(len(sys.argv) == 5):
        if(sys.argv[1] == 'encrypt'):
            print(affineEncrypt(sys.argv[2], int(sys.argv[3]), int(sys.argv[4])))
        elif(sys.argv[1] == 'decrypt'):
            print(affineDecrypt(sys.argv[2], int(sys.argv[3]), int(sys.argv[4])))
        else:
            print("Invalid args\nChoose 'encrypt' or 'decrypt' + word + alpha + beta")
    elif(len(sys.argv) == 1):
        print(affineEncrypt('affinitely', 17, 10))#KRRQXQVAPC
        print(affineDecrypt('KRRQXQVAPC', 17, 10))#affinitely
    else:
        print("Invalid args\n Choose 'encrypt' or 'decrypt' + word + alpha + beta")
  
if __name__== "__main__":
  main()

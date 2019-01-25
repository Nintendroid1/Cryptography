#Encrypts a string using an alphine cipher
def affineEncrypt(plaintext: str, alpha: int, beta: int) -> str:
    plaintext = plaintext.lower()
    ciphertext = []
    for p in plaintext:
        n = ord(p) - 97 #a=97 in ascii, ord converts to ascii
        n = (alpha*n +beta) % 26
        ciphertext.append(chr(n+97).upper()) #chr converts to char
    return ''.join(ciphertext)

print(affineEncrypt('affinitely', 17, 10))#KRRQXQVAPC

def affineDecrypt(ciphertext: str, alpha: int, beta: int) -> str:
    ciphertext = ciphertext.upper()
    plaintext = []
    for c in ciphertext:
        n = ord(c) - 65 #A=65 in ascii
        n = alphaInverse(alpha)*(n-beta)
        plaintext.append(chr(n+65).lower())
    return ''.join(plaintext)

print(affineEncrypt('KRRQXQVAPC', 17, 10))#KRRQXQVAPC

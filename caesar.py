"""
	MATH 4175 - HW 1
	Caesar Cipher Encryptor and Decryptor
	Nathaniel Salazar
"""
import sys

#Encrypts a string using an caesar cipher
def caesarEncrypt(plaintext: str, key: int ) -> str:
    plaintext = plaintext.lower()
    ciphertext = []
    for p in plaintext:
        n = ord(p) - 97 #a=97 in ascii, ord converts to ascii
        n = (n+key) % 26
        ciphertext.append(chr(n+97).upper()) #chr converts to char
    return ''.join(ciphertext)

#Decrypts a string that was encrypted by an caesar cipher and list possible solutions    
def caesarDecrypt(ciphertext: str):
    ciphertext = ciphertext.upper()
    plaintext= []
    for i in range(26):
        for c in ciphertext:
            n = ord(c) - 65 #A=65 in ascii
            n = (n-i)% 26
            plaintext.append(chr(n+65).lower())
        print("Key:%d %s " % (i, ''.join(plaintext)));
        plaintext= []

def main():
    if(len(sys.argv) == 4 and sys.argv[1] == 'encrypt'):
        print(caesarEncrypt(sys.argv[2], int(sys.argv[3])))
    elif(len(sys.argv) == 3 and sys.argv[1] == 'decrypt'):
            print(caesarDecrypt(sys.argv[2]))
    elif(len(sys.argv) == 1):
        print(caesarEncrypt('notsecurewithanykey', 9))#WXCBNLDANFRCQJWHTNH
        caesarDecrypt('WXCBNLDANFRCQJWHTNH')#notsecurewithanykey
    else:
        print("Invalid args\n Choose 'encrypt' + word + key or 'decrypt' + word")
  
if __name__== "__main__":
  main()

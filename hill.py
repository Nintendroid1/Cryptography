"""
	MATH 4175 - HW 1
	Hill Cipher Encryptor and Decryptor
	Nathaniel Salazar
"""

import numpy as np
from numpy.linalg import inv


#Decrypts a string that was encrypted by an Hill cipher and list possible solutions    
#TODO Not complete, need to perform inverse, but returns floats and not in mod 26
def hillDecrypt(ciphertext: str, key, m: int):
    ciphertext = ciphertext.upper()
    ctArray = []
    print("Original Ciphertext:")
    print(ciphertext)
    print("\nKey used:")
    print(key)
    
    for c in ciphertext:
        n = ord(c) - 65 #A=65 in ascii
        ctArray.append(n)
        
    print("\nCiphertext matrix")
    print(ctArray)
    
    keyInverse = inv(key)
    ptArray = np.matmul(ctArray, keyInverse)
    
    plaintext = []
    for i in range(len(ptArray)):
        ptArray[i] = ptArray[i]%26
        plaintext.append(chr(ptArray[i]+97).upper())
        
    print("\nPlaintext matrix:")
    print(ptArray)
    print("\n%s" % (''.join(plaintext)));
    plaintext= []

#Encrypts a string that was using an Hill cipher 
def hillEncrypt(plaintext: str, key, m: int):
    plaintext = plaintext.lower()
    ptArray = []
    
    print("Original Plaintext:")
    print(plaintext)
    print("Key used:")
    print(key)
    for p in plaintext:
        n = ord(p) - 97 #a=97 in ascii
        ptArray.append(n)
    
    print("\nPlaintext matrix:")
    print(ptArray)
    ctArray = np.matmul(ptArray, key)
    
    ciphertext = []
    for i in range(len(ctArray)):
        ctArray[i] = ctArray[i]%26
        ciphertext.append(chr(ctArray[i]+97).upper())
    
    print("\nCiphertext matrix")
    print(ctArray)
    print("\n%s" % (''.join(ciphertext)));
    
def main():
    plaintext = "the"
    ciphertext = "FQV"
    key = np.array([[1,4,10],[0,2,9],[3,1,7]])
    m=3
    hillEncrypt(plaintext, key, m)
    hillDecrypt(ciphertext, key, m)
if __name__== "__main__":
    main()
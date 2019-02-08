"""
	MATH 4175 - HW 3
	Vigenere Cipher encryptor and decryptor
	Nathaniel Salazar
"""
#Decrypts a string that was encrypted by an vigenere cipher and list possible solutions    
def vigenereDecrypt(ciphertext: str, key: str):
    ciphertext = ciphertext.upper()
    key = key.upper()
    plaintext= []
    print("Key used: %s" %(key))
    i=0
    for c in ciphertext:
        n = ord(c) - 65 #A=65 in ascii
        n = (n-(ord(key[i%(len(key))])-65))% 26
        plaintext.append(chr(n+65).lower())
        i += 1
    print("%s" % (''.join(plaintext)));
    plaintext= []

#Encrypts a string that was using an vigenere cipher 
def vigenereEncrypt(plaintext: str, key: str):
    plaintext = plaintext.lower()
    key = key.lower()
    ciphertext= []
    print("Key used: %s" %(key))
    i=0
    for p in plaintext:
        n = ord(p) - 97 #a=97 in ascii
        n = (n+(ord(key[i%(len(key))])-97))% 26
        ciphertext.append(chr(n+97).upper())
        i += 1
    print("%s" % (''.join(ciphertext)));
    
def main():
    ciphertext = "TCXUTSOYMWTDEMXOPKKJOABVXIBABNSCBVISDZPY"
    plaintext = "themostfertilesourceofinsightishindsight"                                                                                                                     
    key = "avtif"
    vigenereDecrypt(ciphertext, key);
    vigenereEncrypt(plaintext, key)
    
    ciphertext = "GVFBQJKHRKFNSGZSUSNCTFRXDJGEESTKHVRIFOEJJVPRQHFMRRFDAAEWFMGGJTOHMYIYNMIGRNXXWOEZIDIGSFECRSTKHRKFNBHSYYEQNTIKRDUVRFZDJTUZYYEPZSEOGFWRNGZIDIGSFECRZYKHRLTDEASMVMNMYYIAJXZTBUJIAACFJKFHKYEJHQCBRZQCOJDIZNYZYVR"
    plaintext = "beforethelawstandsadoorkeepertothisdoorkeepercomesamanfromthecountryandpraysforadmittancetothelawbutthedoorkeepersaysthathecannotgrantadmittanceatthemomenthemanthinksitoverandasksifhewillbeallowedinlater "
    key = "FRANZ"
    vigenereDecrypt(ciphertext, key);
    vigenereEncrypt(plaintext, key)

if __name__== "__main__":
  main()
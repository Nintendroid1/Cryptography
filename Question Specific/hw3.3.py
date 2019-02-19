"""
	MATH 4175 - HW 3
	Script for Problem 3
	Nathaniel Salazar
"""
#Analyzes the frequency of letters in a ciphertext
def frequencyAnalyzer(ciphertext: str):
    ciphertext = ciphertext.lower()
    englishAlphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letterFrequency = [0.0]*26
    for c in ciphertext:
        n = ord(c) - 97 #a=97 in ascii, ord converts to ascii
        letterFrequency[n] += 1
    #for i in range(26):
    #    print("%s: %d" % (englishAlphabet[i], letterFrequency[i]))
    for i in range(len(letterFrequency)):
        letterFrequency[i] /=len(ciphertext)
    return letterFrequency

#Encrypts a string using an caesar cipher
def caesarEncrypt(plaintext: str, key: int ) -> str:
    plaintext = plaintext.lower()
    ciphertext = []
    for p in plaintext:
        n = ord(p) - 97 #a=97 in ascii, ord converts to ascii
        n = (n+key) % 26
        ciphertext.append(chr(n+97).upper()) #chr converts to char
    return ''.join(ciphertext)
    
def mgValue(english, ciphertext):
    englishAlphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    results = [0]*26
    maxIndex = 0
    for i in range(26):
        results[i] = english[i] * ciphertext[i]
    print(sum(results))
    
def main():
    englishFrequency = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070, 0.002, 0.008, 0.040, 0.024, 0.067, 0.075, 0.019, 0.001, 0.060, 0.063, 0.091, 0.028, 0.010, 0.023, 0.001, 0.020, 0.001]
    ciphertext = "GVFBQJKHRKFNSGZSUSNCTFRXDJGEESTKHVRIFOEJJVPRQHFMRRFDAAEWFMGGJTOHMYIYNMIGRNXXWOEZIDIGSFECRSTKHRKFNBHSYYEQNTIKRDUVRFZDJTUZYYEPZSEOGFWRNGZIDIGSFECRZYKHRLTDEASMVMNMYYIAJXZTBUJIAACFJKFHKYEJHQCBRZQCOJDIZNYZYVR"
    Offset0 = []
    Offset1 = []
    Offset2 = []
    Offset3 = []
    Offset4 = []
    
    i=0
    for c in ciphertext:
        if(i == 0):Offset0.append(c)
        if(i == 1):Offset1.append(c)
        if(i == 2):Offset2.append(c)
        if(i == 3):Offset3.append(c)
        if(i == 4):
            Offset4.append(c)
            i=-1
            
        i += 1
    print(''.join(Offset0))#GJFSTJTIJHFWJYIXIFTFYTUDYSWIFYTMYXJFKQQIY                                                                                        
    Frequency0 = frequencyAnalyzer(''.join(Offset0))
    #Shift to Match English Frequency
    Shifted0 = caesarEncrypt(''.join(Offset0), 21)#F
    Frequency0 = frequencyAnalyzer(Shifted0)
    mgValue(englishFrequency, Frequency0)
    
    print(''.join(Offset1))#VKNUFGKFVFDFTIGWDEKNYIVJYERDEKDV  
    Frequency1 = frequencyAnalyzer(''.join(Offset1))
    Shifted1 = caesarEncrypt(''.join(Offset1), 9)#R
    Frequency1 = frequencyAnalyzer(Shifted1)
    mgValue(englishFrequency, Frequency1)
    
    print(''.join(Offset2))#FHSSREHOPMAMOYROICHBEKRTEONICHEM  
    Frequency2 = frequencyAnalyzer(''.join(Offset2))
    Shifted2 = caesarEncrypt(''.join(Offset2), 0)#A
    Frequency2 = frequencyAnalyzer(Shifted2)
    mgValue(englishFrequency, Frequency2)
    
    print(''.join(Offset3))#BRGNXEVERRAGHNNEGRRHQRFUPGGGRRAN  
    Frequency3 = frequencyAnalyzer(''.join(Offset3))
    Shifted3 = caesarEncrypt(''.join(Offset3), 13)#N
    Frequency3 = frequencyAnalyzer(Shifted3)
    mgValue(englishFrequency, Frequency3)
    
    print(''.join(Offset4))#QKZCDSRJQREGMMXZSSKSNDZZZFZSZLSM  
    Frequency4 = frequencyAnalyzer(''.join(Offset4))
    Shifted4 = caesarEncrypt(''.join(Offset4), 5)#Z
    Frequency4 = frequencyAnalyzer(Shifted4)
    mgValue(englishFrequency, Frequency4)


if __name__ == "__main__":
    main()
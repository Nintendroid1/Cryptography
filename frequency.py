"""
	MATH 4175 - HW 3
	Letter Frequency Analyzer
	Nathaniel Salazar
"""
import sys

#Analyzes the frequency of letters in a ciphertext
def frequencyAnalyzer(ciphertext: str):
    ciphertext = ciphertext.lower()
    englishAlphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letterFrequency = [0]*26
    for c in ciphertext:
        n = ord(c) - 97 #a=97 in ascii, ord converts to ascii
        letterFrequency[n] += 1
    for i in range(26):
        print("%s: %d" % (englishAlphabet[i], letterFrequency[i]))
        
def main():
  frequencyAnalyzer('KRLEMPAEPTUAEPKMYTEDDUXUJIZUDKJJICKMEJJWKPYKJJICKMEJDUXUJIZAURPMIRPEKRUDRIPIRJWLEJYUZHIILYYJKZYKRHUEYIRKRCERDKREDXUHPURPAKYPESUYOTKMTOKPTAIHUMEHUMIGJDTEXUVUUREXIKDUDYGMTVJGRDUHYOUHUPTUHUEZJURPWPTUKJJICKMEJDUXUJIZAURPEJYIKRXIJXUDKREDUQGEPUGRDUHYPERDKRCILMIRMUZPYELEKJGHUPIHUMICRKNUEJJPTUZHKRMKZJUYILJICKMKRXIJXUDERDERKREDUQGEPUHKCIHILZHIIL')
  
if __name__== "__main__":
  main()

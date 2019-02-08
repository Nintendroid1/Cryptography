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
    letterFrequency = [0.0]*26
    for c in ciphertext:
        n = ord(c) - 97 #a=97 in ascii, ord converts to ascii
        letterFrequency[n] += 1
    #for i in range(26):
    #    print("%s: %d" % (englishAlphabet[i], letterFrequency[i]))
    for i in range(len(letterFrequency)):
        letterFrequency[i] /=len(ciphertext)
    return letterFrequency

def indexOfCoincidence(frequency: int):
    ic = 0
    for f in frequency:
        ic += f**2
    print(ic)
    
def main():
  #englishFrequency = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070, 0.002, 0.008, 0.040, 0.024, 0.067, 0.075, 0.019, 0.001, 0.060, 0.063, 0.091, 0.028, 0.010, 0.023, 0.001, 0.020, 0.001]
  #indexOfCoincidence(englishFrequency)#0.065601                                                                                                                                                     
  
  ciphertextA='KRLEMPAEPTUAEPKMYTEDDUXUJIZUDKJJICKMEJJWKPYKJJICKMEJDUXUJIZAURPMIRPEKRUDRIPIRJWLEJYUZHIILYYJKZYKRHUEYIRKRCERDKREDXUHPURPAKYPESUYOTKMTOKPTAIHUMEHUMIGJDTEXUVUUREXIKDUDYGMTVJGRDUHYOUHUPTUHUEZJURPWPTUKJJICKMEJDUXUJIZAURPEJYIKRXIJXUDKREDUQGEPUGRDUHYPERDKRCILMIRMUZPYELEKJGHUPIHUMICRKNUEJJPTUZHKRMKZJUYILJICKMKRXIJXUDERDERKREDUQGEPUHKCIHILZHIIL'
  indexOfCoincidence(frequencyAnalyzer(ciphertextA))#0.0674346136339764 
  
  ciphertextB='UXQIPXYKEPRQMDTKFLMNOMIIXYAMQMXVZOVGMVWGVXESWTBKUMLTQIHOWWCQQXEKBRFKTVRHZYEWAPKPLTFIBBZWSWEVTXFMZBPIFSZSYONRPSYIQZQBEMAXYSDBNOQCHPVGTGTBUQABPKNVQMZCYHTKGMOIQXLDBMPOOAHGTLWCAHQBDERVQDSMEIMZWMAXKDSMVPXYRQPEXNPDRPAZXMAXMVDWVRHYWDRHUXLLRUGKEMHRPOCAGEZNTVTSRMZVPIBDDISEUVFZRXABPKBKZSKMNPXDSMCVUXNQCPQCZNYSSSNQAZAVGMQEZNLVVRMNPYHEFOCQTSDYQXESAP'
  indexOfCoincidence(frequencyAnalyzer(ciphertextB))#0.04427365988585835                                                                                                                                          

if __name__== "__main__":
  main()

import sys

def encode(word):
    code = 0
    for i in range(len(word)):
        code += (ord(word[-(i+1)])-ord('a'))* 26 ** i
    return code
        

def decode(x,length):
    digits = []
    word = ''
    for i in range(length):
        digits.append(x % 26)
        x = x // 26
    while(digits):
        word += chr(ord('a')+digits.pop())
    return word

if __name__=="__main__":
    if(str(sys.argv[1]) == "-e" and len(sys.argv)==3):
        print(encode(str(sys.argv[2])))
    elif(str(sys.argv[1]) == "-d" and len(sys.argv)==4):
        print(decode(int(sys.argv[2]), int(sys.argv[3])))
    else:
        print("To encode: decoder.py -e theta(string)")
        print("To decode: decoder.py -d gamma(int) length(int)")
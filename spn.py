def sbox(ptByte: str):
    #0->8
    if(ptByte == "0000"):return "1000"
    
    #1->D
    if(ptByte == "0001"):return "1101" 
    
    #2->6
    if(ptByte == "0010"):return "0110"
    
    #3->F
    if(ptByte == "0011"):return "1111"

    #4->C
    if(ptByte == "0100"):return "1100"

    #5->A
    if(ptByte == "0101"):return "1010"

    #6->9
    if(ptByte == "0110"):return "1001"

    #7->5
    if(ptByte == "0111"):return "0101"

    #8->E
    if(ptByte == "1000"):return "1110"
    
    #9->3
    if(ptByte == "1001"):return "0011"
    
    #A->4
    if(ptByte == "1010"):return "0100"

    #B->0
    if(ptByte == "1011"):return "0000"
    
    #C->1
    if(ptByte == "1100"):return "0001"
    
    #D->7
    if(ptByte == "1101"):return "0111"

    #E->B
    if(ptByte == "1110"):return "1011"
    
    #F->2
    if(ptByte == "1111"):return "0010"
#Substitution Permutation Network
def spn(plaintext: str):
    #XOR with k=0000 0000
    print("u=%s" % (plaintext))
    #Substitution
    lh = plaintext[:4]
    rh = plaintext[4:]
    
    both = []
    both.append(sbox(lh))
    both.append(sbox(rh))

    both = ''.join(both)
    print("v=%s" % (both))
    
    #Permutation
    tau = [0,1,4,5,2,3,6,7]
    ciphertext= []

    for i in range(8):
        ciphertext.append(both[tau[i]])
        
    print("w=%s\n" % (''.join(ciphertext)))
    return ''.join(ciphertext)

def main():
    pt = "10000001" #81 (in hex)
    r1 = spn(pt)
    r2 = spn(r1)
    r3 = spn(r2)
if __name__== "__main__":
  main()
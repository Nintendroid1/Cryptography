"""
	MATH 4175 - HW 4
	LFSR Example
	Nathaniel Salazar
"""

def lfsr(z1,z2,z3,z4):
    sequence = []
    sequence.append(z1)
    sequence.append(z2)
    sequence.append(z3)
    sequence.append(z4)
    
    for i in range(15):
        #z_i+4 = z_i+3 + z_i+1 + z_i
        z5 = (sequence[i+3] + sequence[i+1] + sequence[i]) % 2
        sequence.append(z5)
    
    print(sequence)

def main():
    lfsr(0,0,0,0)
    lfsr(0,0,0,1)
    lfsr(0,0,1,0)
    lfsr(0,0,1,1)
    lfsr(0,1,0,0)
    lfsr(0,1,0,1)
    lfsr(0,1,1,0)
    lfsr(0,1,1,1)
    lfsr(1,0,0,0)
    lfsr(1,0,0,1)
    lfsr(1,0,1,0)
    lfsr(1,0,1,1)
    lfsr(1,1,0,0)
    lfsr(1,1,0,1)
    lfsr(1,1,1,0)
    lfsr(1,1,1,1)

    
if __name__== "__main__":
  main()
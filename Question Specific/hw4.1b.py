"""
	MATH 4175 - HW 4
	1b
	Nathaniel Salazar
"""
import numpy as np
from numpy.linalg import inv

def main():
    matrix = np.array([[4,5],[2,7]])
    for i in range(26):
        for j in range(26):
            pt = []
            pt.append(i)
            pt.append(j)
            results = np.matmul(pt, matrix)
            if(results[0] % 26 == 0 and results[1] % 26 == 0):
                print("i=%d, j=%d" %(i,j))
                print(results)
            

    
if __name__== "__main__":
  main()
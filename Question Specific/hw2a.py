def main():
    #sig_k(42) = (1119, 1449)
    solutions_y_1 = 0
    list_y_1 = []

    solutions_y_2 = 0
    list_y_2 = []

    solutions = 0

    p = 3467
    q = (p-1)//2 # p=2q+1 (Sophie-Germain Prime)
    x = 42
    alpha = 4
    beta = 514
    for a_1 in range(q):
        for b_1 in range(q):
            y_1 = (a_1 + b_1*x)% q
            if(y_1 == 1119):
                solutions_y_1 += 1
                list_y_1.append([a_1, b_1])


    for a_2 in range(q):
        for b_2 in range(q):
            y_2 = (a_2 + b_2*x)% q
            if(y_2 == 1449):
                solutions_y_2 += 1
                list_y_2.append([a_2, b_2])
    
    for pair_1 in list_y_1:
        for pair_2 in list_y_2:
            a_1 = pair_1[0]
            b_1 = pair_1[1]
            a_2 = pair_2[0]
            b_2 = pair_2[1]

            y_1 = (a_1 + b_1*x)% q
            y_2 = (a_2 + b_2*x)% q

            z_1 = (pow(alpha, a_1)*pow(beta, a_2))%p
            z_2 = (pow(alpha, b_1)*pow(beta, b_2))%p
            if((z_1*pow(z_2,x) == (pow(alpha, y_1)*pow(beta, y_2)) % p)):
                solutions += 1
                print(pair_1)
                print(pair_2)

    print("Number of solutions to sig_k(42)=(1119, 1449)= "+str(solutions))

if __name__== "__main__":
  main()
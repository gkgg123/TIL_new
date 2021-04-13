n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11= map(int,input().split())

arr = [[[[[[[[[[list(map(int,input().split())) for _ in range(n2)] for _ in range(n3)] for _ in range(n4)] for _ in range(n5)] for _ in range(n6)] for _ in range(n7)] for _ in range(n8)] for _ in range(n9)] for _ in range(n10)] for _ in range(n11)]


tomato_cnt = 0
total = n1*n2*n3*n4*n5*n6*n7*n8*n9*n10*n11
tomato = []
for A in range(n11):
    for B in range(n10):
        for C in range(n9):
            for D in range(n8):
                for E in range(n7):
                    for F in range(n6):
                        for G in range(n5):
                            for H in range(n4):
                                for I in range(n3):
                                    for J in range(n2):
                                        for K in range(n1):
                                            if arr[A][B][C][D][E][F][G][H][I][J][K] == 1:
                                                tomato.append((A,B,C,D,E,F,G,H,I,J,K))


dK = [-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dJ = [0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dI = [0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dH = [0,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dG = [0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0]
dF = [0,0,0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0]
dE = [0,0,0,0,0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0]
dD = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0]
dC = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1,0,0,0,0]
dB = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1,0,0]
dA = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1]

day = 0
result = 0
while True:
    new_tomato = []
    for A,B,C,D,E,F,G,H,I,J,K in tomato:
        for l in range(22):
            nA = A + dA[l]
            nB = B + dB[l]
            nC = C + dC[l]
            nD = D + dD[l]
            nE = E + dE[l]
            nF = F + dF[l]
            nG = G + dG[l]
            nH = H + dH[l]
            nI = I + dI[l]
            nJ = J + dJ[l]
            nK = K + dK[l]
            if 0<=nA<n11 and 0<=nB<n10 and 0<=nC<n9 and 0<=nD<n8 and 0<=nE<n7 and 0<=nF<n6 and 0<=nG<n5 and 0<=nH<n4 and 0<=nI<n3 and 0<=nJ<n2 and 0<=nK<n1:
                if not arr[nA][nB][nC][nD][nE][nF][nG][nH][nI][nJ][nK]:
                    arr[nA][nB][nC][nD][nE][nF][nG][nH][nI][nJ][nK] = 1
                    new_tomato.append((nA,nB,nC,nD,nE,nF,nG,nH,nI,nJ,nK))

    if len(new_tomato):
        tomato = new_tomato[:]
        day += 1
    else:
        result = day
        for A in range(n11):
            for B in range(n10):
                for C in range(n9):
                    for D in range(n8):
                        for E in range(n7):
                            for F in range(n6):
                                for G in range(n5):
                                    for H in range(n4):
                                        for I in range(n3):
                                            for J in range(n2):
                                                for K in range(n1):
                                                    if arr[A][B][C][D][E][F][G][H][I][J][K] == 0:
                                                        result = -1
        break

print(result)
        
# 9251 LCS
def LCS(SA,SB,SALEN,SBLEN):
    global LCS_list

    for i in range(1,SALEN+1):
        for j in range(1,SBLEN+1):
            if SA[i-1] == SB[j-1]:
                LCS_list[i][j] = LCS_list[i-1][j-1]+1
            else:
                LCS_list[i][j] = max(LCS_list[i-1][j],LCS_list[i][j-1])




A = list(input())
B = list(input())

lenA = len(A)
lenB = len(B)

LCS_list = [[0]*(lenB+1) for _ in range(lenA+1)]

LCS(A,B,lenA,lenB)

print(LCS_list[lenA][lenB])
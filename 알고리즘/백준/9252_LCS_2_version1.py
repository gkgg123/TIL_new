# Longest Common Subsequence
#  최장 공통 부분 수열
def LCSlength(X,Y):
    for i in range(1,len(X)+1):
        for j in range(1,len(Y)+1):
            if X[i-1] == Y[j-1]:
                LCS_ARRAY[i][j] = LCS_ARRAY[i-1][j-1] + 1
            else:
                LCS_ARRAY[i][j] = max(LCS_ARRAY[i][j-1],LCS_ARRAY[i-1][j])
    
def findBackTrack(C,X,Y,i,j):
    if i == 0 or j == 0:
        return ''
    if X[i-1] == Y[j-1]:
        return findBackTrack(C,X,Y,i-1,j-1) + X[i-1]
    if C[i][j-1] > C[i-1][j]:
        return findBackTrack(C,X,Y,i,j-1)
    return findBackTrack(C,X,Y,i-1,j)




string_1 = list(input())
string_2 = list(input())
LCS_ARRAY = [[0]*(len(string_2)+1) for _ in range(len(string_1)+1)]
LCSlength(string_1,string_2)
result = findBackTrack(LCS_ARRAY,string_1,string_2,len(string_1),len(string_2))
print(len(result))
print(result)
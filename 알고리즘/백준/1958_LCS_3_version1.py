def LCS(a,b,c):
    global X,Y,Z
    for i in range(1,X+1):
        for j in range(1,Y+1):
            for k in range(1,Z+1):
                if a[i-1] == b[j-1] and b[j-1] == c[k-1]:
                    LCS_array[i][j][k] = LCS_array[i-1][j-1][k-1] +1
                else:
                    LCS_array[i][j][k] = max(LCS_array[i][j][k], LCS_array[i-1][j][k], LCS_array[i][j-1][k], LCS_array[i][j][k-1])

a = input()
b = input()
c = input()
X = len(a)
Y = len(b)
Z = len(c)
LCS_array = [[[0 for _ in range(Z+1)] for _ in range(Y+1)] for _ in range(X+1)]


LCS(a,b,c)

print(LCS_array[X][Y][Z])
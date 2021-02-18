def solution(A,B):
    result = [[0]*(len(B)+1) for _ in range(len(A)+1)]
    for i in range(1,len(A)+1):
        for j in range(1,len(B)+1):
            if A[i-1] == B[j-1]:
                result[i][j] = result[i-1][j-1] + 1

    return max(map(max,result))

A = input()
B = input()

print(solution(A,B))
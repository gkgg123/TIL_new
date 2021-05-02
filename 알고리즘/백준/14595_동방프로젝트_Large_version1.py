import sys

input = sys.stdin.readline

N = int(input())

M = int(input())
S = [0]*N
E = [0]*N
for _ in range(M):
    x, y = map(lambda x : x-1 ,list(map(int,input().split())))

    S[x] += 1
    E[y] += -1




ind = 0
result = 0
big_cnt = 0
while ind<N:
    if big_cnt:
        big_cnt += S[ind] + E[ind]
        if big_cnt == 0:
            result += 1
        ind += 1
    else:
        if S[ind] == 0:
            result += 1
        else:
            big_cnt += S[ind]
        
        ind += 1
print(result)
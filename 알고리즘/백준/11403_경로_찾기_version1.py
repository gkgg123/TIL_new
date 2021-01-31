# 11403 경로 찾기



import sys

N = int(input())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
for k in range(N):
    for x in range(N):
        for y in range(N):
            if arr[x][k] and arr[k][y]:
                arr[x][y] = 1

for i in range(N):
    print(*arr[i])
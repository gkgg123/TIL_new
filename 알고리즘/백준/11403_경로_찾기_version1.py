# 11403 경로 찾기



N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
for k in range(N):
    for x in range(N):
        for y in range(N):
            if arr[x][k] + arr[k][y] == 2:
                arr[x][y] = 1

for i in range(N):
    print(*arr[i])
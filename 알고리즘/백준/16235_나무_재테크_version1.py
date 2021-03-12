from collections import deque
import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())


AppendList = [list(map(int,input().split())) for _ in range(N)]
tree_info = [[[] for _ in range(N)] for _ in range(N)]
result = 0
forest = [[5]*N for _ in range(N)]

for _ in range(M):
    X,Y,age = map(int,input().split())
    tree_info[X-1][Y-1].append(age)
    result += 1

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
for year in range(K):

    for x in range(N):
        for y in range(N):
            if len(tree_info[x][y])>0:
                temp = []
                summer_forest = 0
                cnt = 0
                limited = len(tree_info[x][y])
                while cnt < limited:
                    age = tree_info[x][y].pop()

                    if forest[x][y] >= age:
                        forest[x][y] -= age
                        temp.append(age+1)
                    else:
                        summer_forest += (age//2)
                        result -= 1
                    cnt += 1
                temp.sort(reverse=True)
                tree_info[x][y].extend(temp)
                forest[x][y] += summer_forest
            forest[x][y] += AppendList[x][y]
    for x in range(N):
        for y in range(N):
            spread_cnt = 0
            if tree_info[x][y]:
                for val in tree_info[x][y]:
                    if val%5 == 0:
                        spread_cnt += 1

            if spread_cnt:
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<N and 0<=ny<N:
                        result += spread_cnt
                        tree_info[nx][ny].extend([1]*spread_cnt)
    print(result)
print(result)

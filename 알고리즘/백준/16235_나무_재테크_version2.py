import sys
input = sys.stdin.readline
N,M,K  = map(int,input().split())
store = [list(map(int,input().split())) for _ in range(N)]
tree_info = [[{} for _ in range(N)] for _ in range(N)]
forest = [[5]*N for _ in range(N)]

tree_cnt = 0
for _ in range(M):
    x,y,age = map(int,input().split())
    tree_info[x-1][y-1][age] = 1
    tree_cnt += 1

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

for _ in range(K):
    for x in range(N):
        for y in range(N):
            if tree_info[x][y]:
                summer_forest = 0
                new_dict = {}

                for age in sorted(tree_info[x][y].keys()):
                    if forest[x][y] >= age * tree_info[x][y][age]:
                        forest[x][y] -= age * tree_info[x][y][age]
                        new_dict[age+1] = tree_info[x][y][age]
                    else:
                        if forest[x][y] // age:
                            new_dict[age+1] = forest[x][y]//age
                            forest[x][y] -=  age*new_dict[age+1]
                            if tree_info[x][y][age] - new_dict[age+1]:
                                summer_forest += (age//2) * (tree_info[x][y][age] - new_dict[age+1])
                                tree_cnt -= (tree_info[x][y][age] - new_dict[age+1])
                        else:
                            summer_forest += (age//2)*tree_info[x][y][age]
                            tree_cnt -= tree_info[x][y][age]
                tree_info[x][y] = new_dict
                forest[x][y] += summer_forest
            forest[x][y] += store[x][y]
    for x in range(N):
        for y in range(N):
            spread_cnt = 0
            for age in tree_info[x][y]:
                if not age%5:
                    spread_cnt += tree_info[x][y][age]
            if spread_cnt:
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx <N and 0<=ny<N:
                        if tree_info[nx][ny].get(1):
                            tree_info[nx][ny][1] += spread_cnt
                        else:
                            tree_info[nx][ny][1] = spread_cnt
                        tree_cnt += spread_cnt
print(tree_cnt)
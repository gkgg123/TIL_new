# 1937 욕심쟁이 판다
def dfs(x,y):
    global N
    stack = [(x,y,0)]
    last_direction = []
    while stack:
        cx,cy,distance = stack.pop()
        flag = True
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx<N and 0<=ny<N:
                if bamboo[cx][cy] < bamboo[nx][ny]:
                    if dp[nx][ny] == -1:
                        stack.append((nx,ny,distance+1))
                    else:
                        if distance + dp[nx][ny] + 1 > dp[x][y]:
                            dp[x][y] = dp[nx][ny] + distance + 1
                           
                    flag = False
        if flag:
            if dp[x][y] < distance + 1:
                dp[x][y] = distance + 1



N = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
bamboo = [list(map(int,input().split())) for _ in range(N)]
dp = [[-1]*N for _ in range(N)]

result = - 1
for x in range(N):
    for y in range(N):
        if dp[x][y] == -1:
            dfs(x,y)
print(max(map(max,dp)))
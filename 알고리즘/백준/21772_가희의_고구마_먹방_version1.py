
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
def dfs(node,time,eat):
    global T,result,R,C
    if time == T:
        result = max(result,eat)
        return
    else:
        result = max(result,eat)
        for i in range(4):
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]
            if 0<=nx<R and 0<=ny<C and not vistied[nx][ny]:
                vistied[nx][ny] = True
                if arr[nx][ny] == 'S':
                    dfs((nx,ny),time+1,eat+1)
                else:
                    dfs((nx,ny),time+1,eat)
                vistied[nx][ny] = False

R,C,T = map(int,input().split())
result = 0
vistied = [[False for _ in range(C)] for _ in range(R)]


arr = []
start = []
for x in range(R):
    temp = list(input())
    for y in range(C):
        if temp[y] == '#':
            vistied[x][y] = True
        elif temp[y] == 'G':
            start = (x,y)
    arr.append(temp)


dx = [-1,1,0,0]
dy = [0,0,-1,1]

dfs(start,0,0)
print(result)
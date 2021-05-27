
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
def dfs(node,time,eat):
    global T,result,R,C
    if time == T:
        result = max(result,eat)
        if result == total_cnt or result == T:
            print(result)
            exit()
        return
    else:
        vistied[node[0]][node[1]] = True
        for i in range(4):
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]
            if 0<=nx<R and 0<=ny<C:
                if vistied[nx][ny]:
                    dfs((nx,ny),time+1,eat)
                elif not vistied[nx][ny] and arr[nx][ny] != '#':
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
total_cnt = 0
for x in range(R):
    temp = list(input())
    for y in range(C):
        if temp[y] == 'G':
            start = (x,y)
        elif temp[y] == 'S':
            total_cnt += 1
    arr.append(temp)


dx = [-1,1,0,0]
dy = [0,0,-1,1]
dfs(start,0,0)
print(result)
# 1987 알파벳

def dfs(x,y,visited,cnt):
    global result,const
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx< R and 0<= ny<C and visited[ord(arr[nx][ny])-const]:
            visited[ord(arr[nx][ny])-const] = False
            dfs(nx,ny,visited,cnt+1)
            visited[ord(arr[nx][ny])-const] = True
    if cnt > result:
        result = cnt

R,C = map(int,input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
arr = [list(input()) for _ in range(R)]
result = 1
visit = [True]*26
const = ord('A')
visit[ord(arr[0][0])-const] = False
dfs(0,0,visit,1)

print(result)
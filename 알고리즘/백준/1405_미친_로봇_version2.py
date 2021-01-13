def dfs(x,y,persent,cnt):
    global revers_persen,N,total
    if arr[x][y] == 1:
        revers_persen += persent
        return
    if cnt == N:
        return
    arr[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if persentlist[i]:
            dfs(nx,ny,persent*persentlist[i],cnt+1)
    arr[x][y] = 0



N,e,w,s,n = map(int,input().split())

e,w,s,n = e/100,w/100,s/100,n/100
dx = [0,0,1,-1]
dy = [1,-1,0,0]
persentlist = [e,w,s,n]
arr = [[0]*29 for _ in range(29)]

revers_persen = 0
dfs(14,14,1,0)
print(f'{1-revers_persen:.10f}')
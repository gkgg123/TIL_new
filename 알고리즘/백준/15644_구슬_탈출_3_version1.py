from collections import deque
def bfs(red,blue):
    stack = deque()

    stack.append((*red,*blue,0,''))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    direction = ['U','D','L','R']
    while stack:
        rx,ry,bx,by,dis,route = stack.popleft()

        if dis >= 10:
            return (-1,'-')

        for i in range(4):
            nrx,nry = rx,ry
            r_p = 0
            while 0<=nrx<N and 0<=nry<M and arr[nrx][nry] != '#' and arr[nrx][nry] != 'O':
                nrx += dx[i]
                nry += dy[i]
                r_p += 1
            nbx,nby = bx,by
            b_p = 0
            while 0<=nbx<N and 0<=nby<M and arr[nbx][nby] != '#' and arr[nbx][nby] != 'O':
                nbx += dx[i]
                nby += dy[i]
                b_p += 1

            if (nbx,nby) == (nrx,nry):
                if arr[nbx][nby] == 'O':
                    continue
                if r_p > b_p:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            elif arr[nbx][nby] == 'O':
                continue
            elif arr[nrx][nry] == 'O':
                return (dis+1,route + direction[i])
            nrx -= dx[i]
            nry -= dy[i]
            nbx -= dx[i]
            nby -= dy[i]
            if not visited[nrx][nry][nbx][nby]:continue
            visited[nrx][nry][nbx][nby] = False
            stack.append((nrx,nry,nbx,nby,dis+1,route+direction[i]))
    return (-1,'-')

N,M = map(int,input().split())


arr = []
blue = []
red = []
for x in range(N):
    temp = list(input())
    for y in range(M):
        if temp[y] == 'B':
            blue = (x,y)
        elif temp[y] == 'R':
            red = (x,y)
    arr.append(temp)


visited = [[[[True for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]


result = bfs(red,blue)
if result[0] != -1:
    print(result[0])
    print(result[1])
else:
    print(result[0])
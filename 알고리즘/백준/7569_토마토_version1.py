# 7569 토마토

M,N,H = map(int,input().split())

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

tomatoarray =[ [list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
# tomato dz dx dy
# H,N,M

total = N*M*H
tomatocnt = 0
tomatos = []
result = -1
day = 0
for x in range(N):
    for y in range(M):
        for z in range(H):
            if tomatoarray[z][x][y] == 1:
                tomatos.append((x,y,z))
                tomatocnt += 1
            elif tomatoarray[z][x][y] == -1:
                total -= 1
if total == tomatocnt:
    result = 0
else:
    while tomatos:
        new_tomato = []
        for x,y,z in tomatos:
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                if 0<=nx<N and 0<=ny<M and 0<=nz<H:
                    if not tomatoarray[nz][nx][ny]:
                        tomatoarray[nz][nx][ny] = 1
                        tomatocnt += 1
                        new_tomato.append((nx,ny,nz))
        day += 1
        if tomatocnt == total:
            result = day
            break
        if len(new_tomato):
            tomatos = [row[:] for row in new_tomato]
        else:
            result = -1
            break
print(result)




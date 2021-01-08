# 7576번 문제 
# 1은 익은 토마토 0은 익지않은 토마토

N,M = map(int,input().split())

tomatoarray = [list(map(int,input().split())) for _ in range(M)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]
tomatocnt = 0
total = N*M
tomato = []
for x in range(M):
    for y in range(N):
        if tomatoarray[x][y] == 1:
            tomato.append((x,y))
            tomatocnt += 1
        elif tomatoarray[x][y] == -1:
            total -= 1
result = -1
day = 0
if total == tomatocnt:
    result = 0
else:
    while tomato:
        new_tomato = []
        for x,y in tomato:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<M and 0<=ny<N:
                    if not tomatoarray[nx][ny]:
                        tomatoarray[nx][ny] = 1
                        new_tomato.append((nx,ny))
                        tomatocnt += 1


        day += 1
        if tomatocnt == total:
            result = day
            break
        if len(new_tomato):
            tomato = [row[:] for row in new_tomato]
        else:
            result = -1
            break



print(result)


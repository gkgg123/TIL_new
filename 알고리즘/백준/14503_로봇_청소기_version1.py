# 14503 로봇 청소기

# r,c 는 r은 북쪽(X) c는 서쪽(Y)
# 동서남북
# sudo
# 1. 현재위치 청소
# 2. 현재 위치에서 왼쪽으로 회전 + 전진 -> 청소 반복
#  없으면 그 방향으로 계속 회전
# 4방향 전부 청소 완료하면 한칸 후진
# 후진이 안되면 멈춤
# d 0,1,2,3 북동남서
# 빈칸은 0, 벽은 1
N,M = map(int,input().split())
robotX,robotY,direction = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
rotate = [3,0,1,2]
visited = [[True] *M for _ in range(N)]
cnt = 1
stack = [(robotX,robotY,direction)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
visited[robotX][robotY] = False
while stack:
    x,y,cu_dire = stack.pop()
    if visited[x][y]:
        visited[x][y] = False
        cnt += 1
    for _ in range(4):
        nx = x + dx[rotate[cu_dire]]
        ny = y + dy[rotate[cu_dire]]
        if 0<= nx <N and 0<= ny<M:
            if visited[nx][ny] and not arr[nx][ny]:
                stack.append((nx,ny,rotate[cu_dire]))
                break
        cu_dire = rotate[cu_dire]
    else:
        reverse_dire = (cu_dire+2)%4
        nx = x + dx[reverse_dire]
        ny = y + dy[reverse_dire]
        if 0<= nx< N and 0<= ny <M and not arr[nx][ny]:
            stack.append((nx,ny,cu_dire))
        else:
            break

print(cnt)

    
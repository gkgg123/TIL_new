# 16236번 아기상어
# N*N 크기에 물고기 M마리 아기상어 1마리
# 아기상어 초기 크기는 2,
# 자기보다 큰 물고기는 먹기x 지나가기 x
# 자기와 같은 물고기 먹기x, 지나가기 o
# 자기보다 작은 물고기 먹기 o 지나가기 o
# 아기상어는 자기 크기 만큼의 횟수만큼 물고기를 먹는다면 크기가 1 증가한다.
# 먹을 수 있는 물고기가 없으면 엄마상어에게 가기
# 먹을 수 있는 물고기가 1마리면 거리가 가장 가까운 물고기를 먹으러간다.
# 먹을수 있는 물고기가 가장 가까운 거리에 있는걸 먹는다. 위 1순위 왼쪽 2순위 위로 정렬 왼쪽으로 정렬 2중정렬
# 1~6 은 물고기 9은 아기상어 위치
dx = [-1,1,0,0]
dy = [0,0,-1,1]
N = int(input())
aquarium = [list(map(int,input().split())) for _ in range(N)]
fishs = []
for x in range(N):
    for y in range(N):
        if aquarium[x][y]:
            if aquarium[x][y] == 9:
                shark_x = x
                shark_y = y
time = 0
shark_size = 2
shark_eat = 0
flag = True
while flag:
    eat_fishs = []
    visited = [[0]*N for _ in range(N)]
    shark = []
    shark.append((shark_x,shark_y,0))
    visited[shark_x][shark_y] = 1
    while shark:
        x,y,distance = shark.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0<= ny< N:
                if not visited[nx][ny]:
                    if aquarium[nx][ny] > shark_size:
                        continue
                    else:
                        visited[nx][ny] = 1
                        if aquarium[nx][ny] == shark_size or aquarium[nx][ny] == 0:
                            shark.append((nx,ny,distance+1))
                        else:
                            shark.append((nx,ny,distance+1))
                            eat_fishs.append((nx,ny,distance+1))
    if not len(eat_fishs):
        break
    else:
        eat_fishs.sort(key=lambda x: (x[2],x[0],x[1]))
        aquarium[shark_x][shark_y] = 0
        shark_x = eat_fishs[0][0]
        shark_y = eat_fishs[0][1]
        shark_eat += 1
        aquarium[shark_x][shark_y] = 9
        time += eat_fishs[0][2]
        if shark_eat == shark_size:
            shark_size += 1
            shark_eat = 0
print(time)
            
    

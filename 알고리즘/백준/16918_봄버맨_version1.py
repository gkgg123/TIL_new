# step 1 봄버맨 폭탄 설치 설치시간 동일
# step 2 정지
# step 3 폭탄이 설치되어 있지않은 모든칸에 폭탄을 설치
# step 4 1초가 지난후 3초전에 설치된 폭탄이 모두 폭발한다.
# step 5 step 3 ~ step 4 반복
dx = [1,-1,0,0]
dy = [0,0,1,-1]

R,C,N = map(int,input().split())
# R은 행 C은 열 N은 초
bomb = [list(input()) for _ in range(R)]
times = [[-1]*C for _ in range(R)]

for x in range(R):
    for y in range(C):
        if bomb[x][y] == 'O':
            times[x][y] = 3

        

for k in range(N):
    bomb_set = set()
    if k%2:
        for x in range(R):
            for y in range(C):
                times[x][y] -= 1
                if bomb[x][y] == '.':
                    times[x][y] = 3
                    bomb[x][y] = 'O'
    else:
        for x in range(R):
            for y in range(C):
                times[x][y] -= 1
                if times[x][y] == 0:
                    bomb_set.add((x,y))
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0<=nx<R and 0<=ny<C:
                            bomb_set.add((nx,ny))
    for nx,ny in bomb_set:
        bomb[nx][ny] = '.'





for rows in range(R):
    print(''.join(bomb[rows]))
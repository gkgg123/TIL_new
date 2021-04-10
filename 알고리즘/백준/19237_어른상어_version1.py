N,M,K = map(int,input().split())
# N 은 격자
# M 은 상어의 수
# K 은 이동횟수

sharks = {}
arr = []
smell = {}
for x in range(N):
    input_list = list(map(int,input().split()))
    for y in range(N):
        if input_list[y]:
           sharks[input_list[y]] = (x,y)
           smell[(x,y)] = [K,input_list[y]]
    arr.append(input_list)
# 0 위 1 아래 2 왼쪽 3 오른쪽

shark_input_move = list(map(int,input().split()))
ind = 1
for shark_init_move in shark_input_move:
    sharks[ind] = (*sharks[ind],shark_init_move-1)
    ind += 1

shark_move = [[],]

for _ in range(M):
    temp = []
    for x in range(4):
        move_input = list(map(lambda x : x-1,map(int,input().split())))
        temp.append(move_input)
    shark_move.append(temp)



time = 0


dx = [-1,1,0,0]
dy = [0,0,-1,1]
while time <= 1000:
    move_shark = {}
    new_smell = {}
    for shark_num in sorted(sharks.keys()):
        x,y,dire = sharks[shark_num]
        shark_move_direction = []
        for i in shark_move[shark_num][dire]:
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <N and 0<=ny <N:
                if not smell.get((nx,ny)):
                    shark_move_direction = (nx,ny,i)
                    break
        else:
            new_dire_list = shark_move[shark_num][dire]
            for new_dire in new_dire_list:
                nx = x + dx[new_dire]
                ny = y + dy[new_dire]
                if 0<=nx<N and 0<=ny<N:
                    if smell[(nx,ny)][1] == shark_num:
                        shark_move_direction = (nx,ny,new_dire)
                        break
        if not new_smell.get((nx,ny)):
            new_smell[(nx,ny)] = [K,shark_num]
            move_shark[shark_num] = shark_move_direction
    for position in smell.keys():
        if not new_smell.get(position):
            if smell[position][0]-1>0:
                new_smell[position] = [smell[position][0]-1,smell[position][1]]
    time += 1
    print(move_shark)
    print(new_smell)
    if time == 14:
        break
    if len(move_shark.keys()) == 1:
        break
    sharks = {}
    for shark_num in move_shark.keys():
        sharks[shark_num] = move_shark[shark_num] 
    smell = {position : new_smell[position] for position in new_smell.keys()}


print(-1 if time == 1001 else time)
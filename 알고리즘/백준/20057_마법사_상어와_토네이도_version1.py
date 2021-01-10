direction = [0,1,2,3]
# dire의 값이 0 : 좌
#  1: 하
#  2: 우
#  3: 상
move_dire = [[0,-1],
[1,0],
[0,1],
[-1,0]]
# 토네이도가 부는 방향 좌 하 우 상
#  -90도 회전 list(zip(*tornado))[::-1]
tornado = [[0,0,2,0,0],
[0,10,7,1,0],
[5,0,0,0,0],
[0,10,7,1,0],
[0,0,2,0,0]]



N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

k = N**2 -1
cnt = 0
number_cnt = 1 
# number_cnt는 현재 방향으로 진행되는 최대거리를 알려주는 것이다.
double_cnt = 0
# 최대거리가 진행되는 횟수를 알려주는 것이다.
cur_cnt = 0
# 현재 이동 횟수이다.
cur_dire = 0 
# 현재 진행 방향이다.
# 이 문제에서 보면 알 수 있듯이, 좌하우상 순서로 진행되면 그 거리는 1,1,2,2,3,3,4,4,5,5,6,6 순으로 진행된다.
# 최대거리가 동일한게 2번 반복되는 것을 알 수 있다.
location = [N//2,N//2]
result = 0

while True:
    # 최대 거리와 현재 이동거리가 같다면 방향이 바뀌어야하는 것이므로, 방향을 바꾸면서 최대거리를 갱신해주는 작업을 해준다.
    if cur_cnt == number_cnt:
        cur_cnt = 0
        double_cnt += 1
        cur_dire = (cur_dire+1)%4
        tornado = list(zip(*tornado))[::-1]
        # -90도 회전을 해주는 간편한 방법이다. 
        if double_cnt == 2:
            # double_cnt가 2라는 것은 최대 이동거리가 동일한게 2번 반복된것이니, 최대 이동거리를 증가시켜줘야한다.
            double_cnt = 0
            number_cnt += 1
    # target_location은 현재 토네이도의 위치인 x에서 y로 갈때 y의 위치이다.
    target_location = [location[0]+move_dire[cur_dire][0],location[1]+move_dire[cur_dire][1]]
    # total_more는 targetloaction에 있는 모래의 양이다.
    total_more = arr[target_location[0]][target_location[1]]
    # torandao로 이동하는 것을 해주는 것이다.
    for i in range(5):
        for j in range(5):
            move_ind = [target_location[0]+i-2,target_location[1]+j-2]
            more = int(tornado[i][j]*arr[target_location[0]][target_location[1]]/100)
            if 0<=move_ind[0]<N and 0<=move_ind[1]<N:
                arr[move_ind[0]][move_ind[1]] += more
            # 만약 범위를 벗어나면, 결과값에 추가해준다.
            else:
                if more:
                    result += more
            # 흩날리고 남은 모래를 a의 모래가 되므로 구해준다.
            total_more -= more
    cur_cnt += 1
    last_location = [location[0]+2*move_dire[cur_dire][0],location[1]+2*move_dire[cur_dire][1]]
    # a의 위치가 범위를 벗어나면, result에 추가해주고, 아니면 해당위치에 모래를 추가해준다.
    if 0<=last_location[0]<N and 0<=last_location[1]<N:
        arr[last_location[0]][last_location[1]] += total_more
    else:
        result += total_more
    location = [location[0]+move_dire[cur_dire][0],location[1]+move_dire[cur_dire][1]]
    arr[location[0]][location[1]] = 0
    if location[0] == 0 and location[1] == 0:
        break
print(result)

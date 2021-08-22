import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def bfs():
    queue = deque()
    queue.append(starts)
    time = 0
    dx = [0, 0, 0, 1, -1]
    dy = [0, 1, -1, 0, 0]
    INF = float('inf')
    visited_list = [[[INF for _ in range(N)] for _ in range(N)] for _ in range(4)]
    while queue:
        len_Q = len(queue)
        for _ in range(len_Q):
            # 현재 위치, 현재영역, 현재영역이 회전한 횟수
            x, y, cur_mod, cur_cnt = queue.popleft()
            for i in range(5):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<N and 0<=ny<N:
                    y_mod = ny//4
                    x_mod = nx//4
                    next_mod = x_mod*K + y_mod
                    # 다음영역을 구하고, 현재영역과 동일하다면, 움직여야할 영역을 현재영역이 회전한 횟수로 해주고
                    # 다음영역이 다르면, 이전번에서 초기화가 됬을거기 때문에 0으로 해서 비교를 해준다.
                    if next_mod == cur_mod:
                        check_cnt = cur_cnt
                    else:
                        check_cnt = 0
                    if rotate_list[check_cnt][nx][ny] != '#':
                        # 만약 도착지점이라한다면, 현재시간에서 + 1을 해서 반환해준다.
                        if rotate_list[check_cnt][nx][ny] == 'E':
                            return time + 1
                        # 현재 영역과  다음영역이 다르면, 다음영역의 회전한 횟수가 0이므로, 다음번의 회전한 횟수는 1이 된다.
                        # 만약 같다면 현재 회전한 횟수에 +1을 해주고 나머지계산을 해준다.
                        if next_mod != cur_mod:
                            next_cnt = 1
                        else:
                            next_cnt = (cur_cnt+1)%4
                        rotate_x = ny+(x_mod*4)-(y_mod*4)
                        rotate_y = (y_mod+1)*4-nx-1+(x_mod*4)
                        # 만약 다음번 상태보다 더 짧은 시간에 갈수 있다면, queue에 넣어준다.
                        if visited_list[next_cnt][rotate_x][rotate_y] > time+1:
                            visited_list[next_cnt][rotate_x][rotate_y] = time + 1
                            queue.append((rotate_x,rotate_y, next_mod,next_cnt))
        time += 1

    return -1
K = int(input())
N = 4*K
rotate_list = []
arr = [list(input()) for _ in range(N)]
# 회전을 담아놓은 배열 0 : 0도 1 : 90도 2 : 180도 3: 270도
rotate_list.append([row[:] for row in arr])
for _ in range(3):
    origin_arr = rotate_list[-1]
    temp = [[0 for _ in range(N)] for _ in range(N)]
    # 4*4 행렬은 각 K의 제곱수 만큼 나온다.
    # 4*4 행렬을 90도 회전을 시켜주면 된다.
    # x축 보정 y+(x_mod*4)-(y_mod*4)
    # y축 보정 (y_mod+1)*4-x-1+(x_mod*4)
    # k = 3일때
    # 0 1 2
    # 3 4 5
    # 6 7 8
    # 로 구역이 나뉘도록 설정
    for ro_ind in range(K*K):
        y_mod = ro_ind%K
        x_mod = ro_ind//K
        for x in range(x_mod*4,(x_mod+1)*4):
            for y in range(y_mod*4,(y_mod+1)*4):
                temp[y+(x_mod*4)-(y_mod*4)][(y_mod+1)*4-x-1+(x_mod*4)] = origin_arr[x][y]
    rotate_list.append([row[:] for row in temp])

starts = []
for x in range(N):
    for y in range(N):
        if arr[x][y] == 'S':
            y_mod = y//4
            x_mod = x//4
            mods = x_mod*K + y_mod
            # 현재위치, 현재 영역, 돌린 횟수를 저장한다.
            starts = [x, y, mods, 0]


print(bfs())



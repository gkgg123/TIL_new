import sys
def find_index(origin):
    global N,M
    min_value = 10001
    min_index = []
    for x in range(N):
        for y in range(M):
            if (x+y)%2:
                if min_value > origin[x][y]:
                    min_value = origin[x][y]
                    min_index = [x,y]
    return min_index
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
if not N%2 and not M%2:
    low_index = find_index(arr)
    result = ''
    front_times = low_index[0]//2
    tail_times = (N-1 -low_index[0])//2
    front_result = ('R'*(M-1)+'D'+'L'*(M-1)+'D')*front_times
    tail_result = ('D'+'L'*(M-1)+'D'+'R'*(M-1))*tail_times

    front_index = [front_times*2,0]
    move = ['D','R','U','R']
    front_direction = [(1,0),(0,1),(-1,0),(0,1)]
    tail_direction = [(-1,0),(0,-1),(1,0),(0,-1)]
    tail_index = [front_index[0]+1,M-1]
    front_cnt = 0
    tail_cnt = 0
    while True:
        nx = front_index[0] + front_direction[front_cnt][0]
        ny = front_index[1] + front_direction[front_cnt][1]
        if nx == low_index[0] and ny == low_index[1]:
            break
        else:
            front_result += move[front_cnt]
        front_cnt = (front_cnt+1)%4
        front_index = [nx,ny]
    if tail_index[0] != front_index[0] or tail_index[1] != front_index[1]:
        while True:
            nx = tail_index[0] + tail_direction[tail_cnt][0]
            ny = tail_index[1] + tail_direction[tail_cnt][1]
            if nx == front_index[0] and ny == front_index[1]:
                tail_result = move[tail_cnt] + tail_result
                break
            else:
                tail_result = move[tail_cnt] + tail_result
            tail_cnt = (tail_cnt+1)%4
            tail_index = [nx,ny]

    result = front_result + tail_result

else:
    if N%2:
        result = ('R'*(M-1)+'D'+'L'*(M-1)+'D')*(N//2)+('R'*(M-1))
    else:
        result = ('D'*(N-1)+'R'+'U'*(N-1)+'R')*(M//2) +('D'*(N-1))
print(result)

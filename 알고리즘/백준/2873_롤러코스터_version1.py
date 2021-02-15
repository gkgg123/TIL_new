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
sys.stdin = open('lo.txt','r')
for tc in range(16):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    if not N%2 and not M%2:
        low_index = find_index(arr)
        result = ''
        front_result = ''
        tail_result = ''
        front_times = low_index[0]//2
        tail_times = (N-1 -low_index[0])//2
        for ind in range(1,M*front_times*2+1):
            a = ind//M
            b = ind%M
            if not b:
                front_result += 'D'
            else:
                if a%2:
                    front_result += 'L'
                else:
                    front_result += 'R'
        for ind in range(1,M*tail_times*2):
            a = ind//M
            b = ind%M
            if not b:
                tail_result += 'D'
            else:
                if a%2:
                    tail_result += 'R'
                else:
                    tail_result += 'L'
        if tail_times:
            tail_result = 'D'+tail_result
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
            result = ''
            for ind in range(1,N*M):
                a = ind//M
                b = ind%M
                if not b:
                    result += 'D'
                else:
                    if a%2:
                        result += 'L'
                    else:
                        result += 'R'
        else:
            result = ''
            for ind in range(1,N*M):
                a = ind//N
                b = ind%N
                if not b:
                    result += 'R'
                else:
                    if a%2:
                        result += 'U'
                    else:
                        result += 'D'   
    print(tc)
    print(result)

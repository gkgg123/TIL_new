from collections import deque
def find_passenger(start,K):
    stack = deque()
    stack.append((*start,K))
    visited = [[True]*N for _ in range(N)]
    visited[start[0]][start[1]] = False
    if passenger_arr[start[0]][start[1]] < 0:
        result = [start[0],start[1],K,passenger_arr[start[0]][start[1]]]
        passenger_arr[start[0]][start[1]] = 0
        return result

    candidate = []
    while stack:
        x,y,fuel = stack.popleft()
        if fuel <= 0:
            return False
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if passenger_arr[nx][ny] <=0 and visited[nx][ny]:
                    visited[nx][ny] = False
                    stack.append((nx,ny,fuel-1))
                    if passenger_arr[nx][ny] < 0:
                        candidate.append([nx,ny,fuel-1,passenger_arr[nx][ny]])
    if candidate:
        candidate.sort(key=lambda x : (-x[2],x[0],x[1]))
        result = candidate[0]
        passenger_arr[result[0]][result[1]] = 0
        return result
    else:
        return False

def find_destination(passenger):
    stack = deque()
    stack.append((passenger[0],passenger[1],passenger[2]))
    destination = destination_dict[passenger[-1]]
    visited = [[True]*N for _ in range(N)]
    visited[passenger[0]][passenger[1]] = False
    init_fuel = passenger[2]
    while stack:
        x,y,fuel = stack.popleft()
        if fuel <= 0:
            return False
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx <N and 0<=ny<N:
                if passenger_arr[nx][ny] <=0 and visited[nx][ny]:
                    visited[nx][ny] = False
                    stack.append((nx,ny,fuel-1))
                    if (nx,ny) == destination:
                        fuel = 2*init_fuel - fuel + 1
                        result = [nx,ny,fuel]
                        return result

N,M,K = map(int,input().split())

passenger_arr = [list(map(int,input().split())) for _ in range(N)]
destination_dict = {}
taxi = list(map(lambda x : x-1 ,map(int,input().split())))
ind = 2



dx = [-1,0,1,0]
dy = [0,-1,0,1]

for _ in range(M):
    start_x,start_y,end_x,end_y = map(lambda x : x-1 ,map(int,input().split()))
    passenger_arr[start_x][start_y] = -ind
    destination_dict[-ind] = (end_x,end_y)
    ind += 1


answer = 0
cnt = 0
while cnt <M:
    if K == 0:
        answer = -1
        break
    passenger = find_passenger(taxi,K)
    if not passenger:
        answer = -1
        break
    destination = find_destination(passenger)
    if not destination:
        answer = -1
        break
    taxi = [destination[0],destination[1]]
    K = destination[-1]
    cnt += 1


if answer == -1:
    print(answer)
else:
    print(K)


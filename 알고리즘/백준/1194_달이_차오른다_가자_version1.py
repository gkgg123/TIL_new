from collections import deque
N, M = map(int,input().split())



lower_dict = {}
upper_dict = {}

for i in range(6):
    lower_dict[chr(ord('a')+i)] = i
    upper_dict[chr(ord('A')+i)] = i

start = []
arr = []
for x in range(N):
    input_list = list(input())
    for y in range(M):
        if input_list[y] == '0':
            start = (x,y)
    arr.append(input_list)


stack = deque()
stack.append((0,start,0))
flag = True
result = []
INF = float('inf')
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[[INF for _ in range(M)] for _ in range(N)] for _ in range(64)]
visited[0][start[0]][start[1]] = 0
while stack:
    time,cur_node,state = stack.popleft()
    x,y = cur_node
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M:
            if arr[nx][ny] != '#' and visited[state][nx][ny] == INF:
                if arr[nx][ny] in upper_dict.keys():
                    if state & 1<<upper_dict[arr[nx][ny]]:
                        visited[state][nx][ny] = time + 1
                        stack.append((time+1,(nx,ny),state))
                elif arr[nx][ny] in lower_dict.keys():
                    visited[state][nx][ny] = time + 1
                    new_state = state | 1<< lower_dict[arr[nx][ny]]
                    visited[new_state][nx][ny] = time + 1
                    stack.append((time+1,(nx,ny),new_state))
                else:
                    if arr[nx][ny] == '1':
                        flag = False
                        result.append(time+1)
                        break
                    visited[state][nx][ny] = time + 1
                    stack.append((time+1,(nx,ny),state))
    if not flag:
        break

if flag:
    print(-1)
else:
    print(min(result))
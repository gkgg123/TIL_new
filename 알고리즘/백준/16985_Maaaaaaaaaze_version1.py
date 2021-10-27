import sys
from itertools import permutations,product
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
def bfs():
    visited = [[[True for _ in range(5)] for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = False
    queue = deque()
    queue.append((0,0,0,0))
    while queue:
        z,x,y,cnt = queue.popleft()
        if cnt >=answer:
            return 0 
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<=nx<5 and 0<=ny<5 and 0<=nz<5:
                if maze[nz][nx][ny] and visited[nz][nx][ny]:
                    visited[nz][nx][ny] = False
                    queue.append((nz,nx,ny,cnt+1))
                    if (nz,nx,ny) == (4,4,4):
                        return cnt+1
    return 0
        
def rotate_90(bo):
    new_board = [[0 for _ in range(5)] for _ in range(5)]
    for x in range(5):
        for y in range(5):
            new_board[y][4-x] = bo[x][y]
    return new_board
def rotate(ind,cnt):
    ro_board = [row[:] for row in  boards[ind][0]]
    while cnt:
        ro_board = rotate_90(ro_board)
        cnt -= 1
    return ro_board
def make_maze(order):
    for rot_nums in product([0, 1, 2, 3], repeat=5):
        temp = []
        for ind in range(5):
            temp.append(boards[order[ind]][rot_nums[ind]])
        yield temp
boards = [[] for _ in range(5)]

for ind in range(5):
    temp = [list(map(int,input().split())) for _ in range(5)]
    boards[ind].append(temp)

    for cnt in range(1,4):
        boards[ind].append(rotate(ind,cnt))



dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

answer = float('inf')
for orders in permutations(range(5)):
    for maze in make_maze(orders):
        if maze[0][0][0] == 0 or maze[4][4][4] == 0:
            continue
        result = bfs()
        if result:
            answer = min(result,answer)
            if answer == 12:
                print(12)
                exit()
        

print(-1 if answer == float('inf') else answer)

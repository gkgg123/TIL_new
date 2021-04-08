def check(dx,dy):
    for x in range(rotate_N):
        for y in range(rotate_M):
            if rotate_puzzle[x][y] == '0':
                continue
            nx = x + dx
            ny = y + dy
            if (0<=nx<fix_N and 0<=ny<fix_M and fix_puzzle[nx][ny] =='1'):
                return False
    return True

puzzles = []

fix_N,fix_M = map(int,input().split())

fix_puzzle = [list(input()) for _ in range(fix_N)]

result = float('inf')
rotate_N,rotate_M = map(int,input().split())
rotate_puzzle = [list(input()) for _ in range(rotate_N)]

a_set = set()

min_X_A = float('inf')
min_Y_A = float('inf')
max_X_A = 0
max_Y_A = 0
for _ in range(4):
    b_set = set()


    for dx in range(-50,0+fix_N):
        for dy in range(-50,0+fix_M):            
            if check(dx,dy):
                row = max(fix_N-1,dx+rotate_N-1) - min(0,dx) + 1
                col = max(fix_M -1 , dy + rotate_M-1) - min(0,dy) + 1
                result = min(result,row*col)
    
    rotated = [[0]*rotate_N for _ in range(rotate_M)]
    for x in range(rotate_N):
        for y in range(rotate_M):
            rotated[y][rotate_N-x-1] = rotate_puzzle[x][y]

    rotate_M,rotate_N = rotate_N,rotate_M
    rotate_puzzle = [row[:] for row in rotated]


print(result)
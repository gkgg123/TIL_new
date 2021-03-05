import sys

input = sys.stdin.readline

N = int(input())

arr = [[0]*101 for _ in range(101)]
dx = [1,0,-1,0]
dy = [0,-1,0,1]
for _ in range(N):
    x,y,dire,gener = map(int,input().split())
    # dire 0 ->1
    # 1->2
    # 2->3
    # 3->0
    move_list = [dire]
    arr[y][x] = 1
    for _ in range(gener):
        temp = []
        for i in range(len(move_list)-1,-1,-1):
            temp.append((move_list[i]+1)%4)
        move_list.extend(temp)
    for i in move_list:
        nx = x + dx[i]
        ny = y + dy[i]
        arr[ny][nx] = 1
        x,y  = nx,ny
result = 0
for y in range(100):
    for x in range(100):
        if arr[y][x] + arr[y+1][x] + arr[y][x+1] + arr[y+1][x+1] == 4:
            result += 1
print(result)
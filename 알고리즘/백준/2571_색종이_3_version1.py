import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = [[0 for _ in range(101)] for _ in range(100)]
for _ in range(N):
    ax,ay = map(int,input().split())

    for x in range(ax,ax+10):
        for y in range(ay,ay+10):
            arr[x][y] = 1


for x in range(1,100):
    for y in range(100):
        if arr[x][y]:
            arr[x][y] += arr[x-1][y]

result = 0
for x in range(100):
    for start_y in range(100):
        x_width = float('inf')
        for end_y in range(start_y,100):
            if x_width > arr[x][end_y]:
                x_width = arr[x][end_y]
            if not x_width:
                break
            area = x_width * (end_y - start_y+1)
            result = max(area,result)

print(result)

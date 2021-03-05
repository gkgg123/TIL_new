import sys

input = sys.stdin.readline

N = int(input())

arr =[ list(map(int,input().split())) for _ in range(N)]

max_arr = [[0]*3 for _ in range(2)]
min_arr = [[0]*3 for _ in range(2)]

max_arr[0][0] = min_arr[0][0] = arr[0][0]
max_arr[0][1] = min_arr[0][1] = arr[0][1]
max_arr[0][2] = min_arr[0][2] = arr[0][2]

for i in range(1,N):
    max_arr[1][0] = arr[i][0] + max(max_arr[0][0],max_arr[0][1])
    max_arr[1][1] = arr[i][1] + max(max_arr[0][0],max_arr[0][1],max_arr[0][2])
    max_arr[1][2] = arr[i][2] + max(max_arr[0][1],max_arr[0][2])
    min_arr[1][0] = arr[i][0] + min(min_arr[0][0],min_arr[0][1])
    min_arr[1][1] = arr[i][1] + min(min_arr[0][0],min_arr[0][1],min_arr[0][2])
    min_arr[1][2] = arr[i][2] + min(min_arr[0][1],min_arr[0][2])

    for y in range(3):
        max_arr[0][y] = max_arr[1][y]
        min_arr[0][y] = min_arr[1][y]

print(max(max_arr[0]),min(min_arr[0]))
import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]
result = float('inf')
answer = []
for idx1 in range(N):
    max_value = 0
    x1,y1 = arr[idx1]
    for idx2 in range(N):
        if idx1 == idx2:continue
        x2,y2 = arr[idx2]
        distance = (x1-x2)**2 + (y1-y2)**2
        max_value = max(distance,max_value)

    if result > max_value:
        answer = [x1,y1]
        result = max_value
print(*answer)
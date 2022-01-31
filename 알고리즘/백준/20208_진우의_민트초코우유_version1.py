import sys
from itertools import permutations
def input():
    return sys.stdin.readline().rstrip()

def distance(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

N,H,up_H = map(int,input().split())


arr = [list(map(int,input().split())) for _ in range(N)]

start = (0,0)
mint = []
for x in range(N):
    for y in range(N):
        if arr[x][y] == 1:
            start = (x,y)
            arr[x][y] = 0
        elif arr[x][y] == 2:
            mint.append((x,y))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = 0



for perm in permutations(mint):

    cur_node = start
    cur_H = H
    cnt = 0
    for next_node in perm:
        next_distance = distance(cur_node,next_node)
        go_home = distance(next_node,start)

        if cur_H >= next_distance:
            cnt += 1
            cur_H = cur_H -next_distance + up_H

            if cur_H >= go_home:
                result = max(result,cnt)

            cur_node = next_node
        else:
            break

print(result)

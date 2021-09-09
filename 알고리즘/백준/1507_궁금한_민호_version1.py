import sys

def input():
    return sys.stdin.readline().rstrip()
def floyd():
    result = 0
    for mid in range(N):
        for start in range(N):
            for end in range(N):
                if start == end or end == mid or mid == start or start>end:continue
                if arr[start][end] == arr[start][mid] + arr[mid][end]:
                    if (start,end) in edge_list:
                        edge_list.remove((start,end))
                if arr[start][end] > arr[start][mid] + arr[mid][end]:
                    return -1

    for x,y in edge_list:
        result += arr[x][y]
    return result
N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]
edge_list = set()
for i in range(N):
    for j in range(N):
        if i ==j or i>j: continue
        edge_list.add((i,j))

print(floyd())

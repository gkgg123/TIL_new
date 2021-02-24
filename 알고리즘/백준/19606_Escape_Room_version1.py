from collections import deque
def bfs():
    global N,M
    stack = deque()
    stack.append((N,M))

    while stack:
        x,y = stack.pop()
        if x == 1 and y == 1:
            return 'yes'
        if dict_array.get(x*y):
            for nodes in dict_array[x*y]:
                stack.append(nodes)
            del dict_array[x*y]
    return 'no'

N = int(input())
M = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]
dict_array = {}
for x in range(N):
    for y in range(M):
        if dict_array.get(arr[x][y]):
            dict_array[arr[x][y]].append((x+1,y+1))
        else:
            dict_array[arr[x][y]] = [(x+1,y+1)]

if dict_array.get(N*M):
    print(bfs())
else:
    print('no')

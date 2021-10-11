import sys
from itertools import combinations
from collections import deque
def input():
    return sys.stdin.readline().rstrip()


arr = [list(input()) for _ in range(5)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = 0
for combi in combinations(range(25),7):
    s_cnt = 0
    for num in combi:
        x,y = num//5,num%5
        if arr[x][y] == 'S':
            s_cnt += 1
    if s_cnt < 4:
        continue

    queue = deque()
    queue.append(combi[0])
    visited_set = set([combi[0]])
    cnt = 1
    while queue:
        num = queue.popleft()
        x,y = num//5, num%5
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<5 and 0<=ny<5:
                next_num = nx*5 + ny
                if next_num in combi and next_num not in visited_set:
                    queue.append(next_num)
                    visited_set.add(next_num)
                    cnt += 1
    if cnt == 7:
        answer += 1

print(answer)
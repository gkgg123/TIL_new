# 2251 물통
#  A,B,C 
#  앞의 두 물통은 비어 있고, 세번째 물통은 가득 차 있다.
# A 물통이 비어있을때 세번째 물통에 담겨 있을 수 있는 물의 양을 구해내시오.
import collections 
max_Bowl = list(map(int,input().split()))
current_bowl = [0,0,max_Bowl[2]]
visited = [[[False]*(max_Bowl[2]+1) for _ in range(max_Bowl[1]+1)] for _ in range(max_Bowl[0]+1)]
# A,B,C
que = collections.deque()
que.appendleft((0,0,max_Bowl[2]))
result = set()
result.add(max_Bowl[2])
while que:
    cureent_water = que.popleft()
    if visited[cureent_water[0]][cureent_water[1]][cureent_water[2]]:
        continue
    if cureent_water[0] == 0:
        result.add(cureent_water[2])
    visited[cureent_water[0]][cureent_water[1]][cureent_water[2]] = True
    # A->B
    if cureent_water[0]+cureent_water[1] >= max_Bowl[1]:
        que.append((cureent_water[0]+cureent_water[1]-max_Bowl[1],max_Bowl[1],cureent_water[2]))
    else:
        que.append((0,cureent_water[0]+cureent_water[1],cureent_water[2]))
    # A->C
    if cureent_water[0]+cureent_water[2] >= max_Bowl[2]:
        que.append((cureent_water[0]+cureent_water[2]-max_Bowl[2],cureent_water[1],max_Bowl[2]))
    else:
        que.append((0,cureent_water[1],cureent_water[0]+cureent_water[2]))
    # B->C
    if cureent_water[1]+cureent_water[2] >= max_Bowl[2]:
        que.append((cureent_water[0],cureent_water[1]+cureent_water[2]-max_Bowl[2],max_Bowl[2]))
    else:
        que.append((cureent_water[0],0,cureent_water[1]+cureent_water[2]))
    # B->A
    if cureent_water[1]+cureent_water[0] >= max_Bowl[0]:
        que.append((max_Bowl[0],cureent_water[1]+cureent_water[0]-max_Bowl[0],cureent_water[2]))
    else:
        que.append((cureent_water[1]+cureent_water[0],0,cureent_water[2]))
    # C->A
    if cureent_water[2] + cureent_water[0] >= max_Bowl[0]:
        que.append((max_Bowl[0],cureent_water[1],cureent_water[2]+cureent_water[0]-max_Bowl[0]))
    else:
        que.append((cureent_water[2]+cureent_water[0],cureent_water[1],0))
    # C->B
    if cureent_water[2] + cureent_water[1] >= max_Bowl[1]:
        que.append((cureent_water[0],max_Bowl[1],cureent_water[2]+cureent_water[1]-max_Bowl[1]))
    else:
        que.append((cureent_water[0],cureent_water[2]+cureent_water[1],0))

result = sorted(list(result))
print(*result)
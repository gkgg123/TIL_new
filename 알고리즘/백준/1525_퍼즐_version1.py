from collections import deque
def bfs(idx):
    queue = deque()
    queue.append((idx,0,arr[:]))
    visited = set()
    visited.add(''.join(arr))
    while queue:
        zero_idx,dis,cur_state = queue.popleft()

        if ''.join(cur_state) == '123456780':
            return dis

        for i in range(4):
            next_idx = zero_idx + d[i]
            if( 0<=next_idx<9 and i <2) or  (next_idx//3 == zero_idx//3 and i>=2):
                new_arr = cur_state[:]
                new_arr[next_idx],new_arr[zero_idx] = new_arr[zero_idx],new_arr[next_idx]
                if ''.join(new_arr) in visited:
                    continue
                visited.add(''.join(new_arr))
                queue.append((next_idx,dis+1,new_arr[:]))

    return -1


arr = []

for _ in range(3):
    arr.extend(list(input().split()))

d = [-3,3,1,-1]

zero_idx = -1

for i in range(9):
    if arr[i] == '0':
        zero_idx = i

print(bfs(zero_idx))


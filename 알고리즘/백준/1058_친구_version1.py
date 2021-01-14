# 1058 친구

def dfs(idx):
    global N
    visited = [True]*N
    visited[idx] = False
    stack = [(idx,0)]
    cnt = -1

    while stack:
        cu_x,both_person = stack.pop()
        for x in range(N):
            if arr[cu_x][x] == 'Y':
                if visited[x] and both_person <= 1:
                    visited[x] = False
                    stack.append((x,both_person+1))
        cnt += 1
    return cnt
N = int(input())

arr = [list(input()) for _ in range(N)]
max_number = 0
for i in range(N):
    temp = dfs(i)
    max_number = max(max_number,temp)

print(max_number)
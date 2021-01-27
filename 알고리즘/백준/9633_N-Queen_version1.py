def nqueen(x):
    global cnt
    for i in range(x+1):
        if x != i:
            if (visited[i] == visited[x]) or (abs(visited[i]-visited[x]) == abs(i-x)):
                return
    if x == N-1:
        cnt += 1
        return
    for i in range(N):
        visited[x+1] = i
        nqueen(x+1)



N = int(input())
cnt = 0
visited = [-1] * N
for i in range(N):
    visited[0] = i
    nqueen(0)
print(cnt)
T = int(input())
dx = [-2,-1,1,2,2,1,-1,-2]
dy = [-1,-2,-2,-1,1,2,2,1]
for tc in range(T):
    l = int(input())
    array = [list(map(int,input().split())) for _ in range(2)]

    start = array[0][:]
    end = array[1][:]
    if start == end:
        print(0)
    else:
        result = 0
        visited = [[0]*l for _ in range(l)]
        visited[start[0]][start[1]] = 1
        stack = []
        stack.append((start[0],start[1],0))
        while stack:
            x,y,cnt = stack.pop(0)
            if x == end[0] and y == end[1]:
                result = cnt
                break
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<l and 0<=ny<l:
                    if not visited[nx][ny]:
                        visited[nx][ny] = 1
                        stack.append((nx,ny,cnt+1))
        print(result)
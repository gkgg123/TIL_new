import sys
input = sys.stdin.readline
while True:
    N,M = map(int,input().split())
    if not N+M:
        break

    arr = [list(map(int,input().split())) for _ in range(N)]
    maze = [[0 for _ in range(M)] for _ in range(N)]
    for y in range(M):
        maze[0][y] = arr[0][y]
    for x in range(1,N):
        for y in range(M):
            if arr[x][y]:
                maze[x][y] = maze[x-1][y] + arr[x][y]

    result = 0

    for x in range(N):
        col_idx = 0
        stack = []
        while col_idx<M:
            if stack:
                if stack[-1] <= maze[x][col_idx]:
                    stack.append(maze[x][col_idx])
                    col_idx += 1
                else:
                    size_stack = len(stack)
                    min_value = stack[-1]
                    cu_idx = -1
                    for i in range(size_stack):
                        result = max(result,min_value*(i+1))
                        cu_idx -= 1
                        if abs(cu_idx)<=size_stack and min_value > stack[cu_idx]:
                            min_value = stack[cu_idx]
                    

                    if maze[x][col_idx]:
                        stack.append(maze[x][col_idx])
                    else:
                        stack.clear()
                    col_idx += 1

            else:
                if maze[x][col_idx]:
                    stack.append(maze[x][col_idx])
                col_idx += 1
        if stack:
            size_stack = len(stack)
            min_value = stack[-1]
            cu_idx = -1
            for i in range(size_stack):
                result = max(result,min_value*(i+1))
                cu_idx -= 1
                if abs(cu_idx)<=size_stack and min_value > stack[cu_idx]:
                    min_value = stack[cu_idx]

    print(result)

        



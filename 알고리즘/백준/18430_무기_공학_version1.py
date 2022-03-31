import sys

def input():
    return sys.stdin.readline().rstrip()
def outOfBound(x,y):
    if 0<=x<N and 0<=y<M:
        return False
    return True
def backtracking(x,y,count):
    global answer
    if x == N:
        answer = max(answer,count)
        return

    if y == M:
        backtracking(x+1,0,count)
    elif visited[x][y]:
        visited[x][y] = False
        for idx in range(4):
            positions = dire[idx]
            strength = namu[x][y]*2
            for dx,dy in positions:
                nx = x + dx
                ny = y + dy
                if outOfBound(nx,ny):
                    break
                if not visited[nx][ny]:
                    break
            else:
                for dx,dy in positions:
                    nx = x + dx
                    ny = y + dy
                    strength += namu[nx][ny]
                    visited[nx][ny] = False
                backtracking(x,y+1,count+strength)
                for dx,dy in positions:
                    nx = x + dx
                    ny = y + dy
                    visited[nx][ny] = True
        visited[x][y] = True
        backtracking(x,y+1,count)
    else:
        backtracking(x,y+1,count)


N,M = map(int,input().split())


namu = [list(map(int,input().split())) for _ in range(N)]
answer = 0
visited = [[True for _ in range(M)] for _ in range(N)]
dire = [
        [[1,0],[0,-1]],
        [[-1,0],[0,-1]],
        [[-1,0],[0,1]],
        [[1,0],[0,1]]
 ]
backtracking(0,0,0)

print(answer)
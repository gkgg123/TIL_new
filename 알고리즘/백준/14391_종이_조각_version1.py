# import sys

# def input():
#     return sys.stdin.readline().rstrip()
def Innerbound(x,y):
    if 0<=x<N and 0<=y<M:
        return True
    else:
        return False

def dfs(idx,bit,total):
    global result
    if bit == 2**(N*M)-1:
        result = max(result,total)
        return
    else:
        if 2**idx&bit:
            dfs(idx+1,bit,total)
        else:
            x,y = idx//M, idx%M
            nx,ny = x,y
            temp_bit = bit
            temp_num = 0
            while Innerbound(nx,ny):
                if visited[nx][ny]:
                    next_idx = nx*M + ny
                    visited[nx][ny] = False
                    temp_bit = temp_bit|(2**next_idx)
                    temp_num = temp_num*10 + arr[nx][ny]
                    nx = nx + 1
                    ny = ny
                else:
                    break
            for rx in range(nx-1,x-1,-1):
                dfs(idx+1,temp_bit,total + temp_num)
                temp_num = temp_num//10
                next_idx = rx*M + y
                temp_bit = temp_bit^(2**next_idx)
                visited[rx][y] = True
            nx,ny = x,y
            temp_bit = bit
            temp_num = 0
            while Innerbound(nx,ny):
                if visited[nx][ny]:
                    next_idx = nx*M + ny
                    visited[nx][ny] = False
                    temp_bit = temp_bit|(2**next_idx)
                    temp_num = temp_num*10 + arr[nx][ny]
                    nx = nx
                    ny = ny + 1
                else:
                    break
            for ry in range(ny-1,y-1,-1):
                dfs(idx+1,temp_bit,total + temp_num)
                temp_num = temp_num//10
                next_idx = x*M + ry
                temp_bit = temp_bit^(2**next_idx)
                visited[x][ry] = True


N,M = map(int,input().split())

arr = [list(map(int,list(input()))) for _ in range(N)]

visited = [[True for _ in range(M)] for _ in range(N)]
result = 0
dfs(0,0,0)
print(result)
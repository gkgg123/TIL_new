N,M = map(int,input().split())

arr = [list(map(int,list(input()))) for _ in range(N)]
result = 0
max_size = min(N,M)

for x in range(N):
    for y in range(M):
        if result == max_size:
            break
        if arr[x][y] == 1:
            for sizes in range(result,max_size+1):
                temp = 0
                for dx in range(sizes):
                    for dy in range(sizes):
                        if 0<=x+dx<N and 0<=y+dy<M: 
                            temp += arr[x+dx][y+dy]
                if temp == sizes**2:
                    result = sizes
                else:
                    break
print(result**2)


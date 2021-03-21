N, M = map(int,input().split())
total_length = N*M
so_list = [M]*N

cnt = 0
for k in range(N):
    if so_list[k]%N:
        cnt += so_list[k]//N
    else:
        cnt = cnt + so_list[k]//N-1
    so_list[k] -= so_list[k]//N*N

if sum(so_list):
    ind = 0
    temp = 0
    while ind <N:
        temp += so_list[ind]
        if temp == N:
            temp = 0
        elif temp >N:
            cnt += 1
            temp -= N
        ind += 1
        
print(cnt)
import sys

def input():
    return sys.stdin.readline().rstrip()


while True:
    N,K = map(int,input().split())
    if not N+K:
        break

    input_list = [-1]+ list(map(int,input().split()))

    cnt = -1
    group_idx = [-1 for _ in range(N+1)]
    target_idx = -1
    for idx in range(1,N+1):
        if input_list[idx] == K:
            target_idx = idx
        
        if input_list[idx-1] + 1 != input_list[idx]:
            cnt += 1
        
        group_idx[idx] = cnt

    result = 0
    for idx in range(1,N+1):
        if group_idx[idx] != group_idx[target_idx] and group_idx[group_idx[idx]] == group_idx[group_idx[target_idx]]:
            result += 1
    print(result)
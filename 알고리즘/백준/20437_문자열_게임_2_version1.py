import sys
def input():
    return sys.stdin.readline().rstrip()


T = int(input())

for _ in range(T):
    W = list(input())
    N = len(W)
    K = int(input())
    alpha_list = [[] for _ in range(26)]
    max_cnt = 0
    for idx,alpha in enumerate(W):
        alpha_idx = ord(alpha) - ord('a')
        alpha_list[alpha_idx].append(idx)
    max_length = 0
    min_length = float('inf')
    flag = True
    for alpha in range(26):
        if len(alpha_list[alpha])<K:continue
        left = 0
        flag = False
        right = K-1
        while right<len(alpha_list[alpha]):
            max_length = max(max_length,alpha_list[alpha][right] - alpha_list[alpha][left] + 1)
            min_length = min(min_length,alpha_list[alpha][right] - alpha_list[alpha][left] + 1 )
            left+=1
            right+=1
    if flag:
        print(-1)
    else:
        print(min_length,max_length)
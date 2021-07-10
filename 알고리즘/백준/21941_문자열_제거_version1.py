import sys

def input():
    return sys.stdin.readline().rstrip()

def dfs(idx):
    if idx >= N:
        return 0

    if dp[idx] != -1:
        return dp[idx]
    max_value = 0
    for string_key in score_dict.keys():
        score,len_string = score_dict[string_key]
        if idx + len_string-1<N:
            for check_idx in range(len_string):
                if input_string[check_idx+idx] != string_key[check_idx]:
                    break
            else:
                max_value = max(max_value,score + dfs(idx+len_string))
    max_value = max(max_value,1+dfs(idx+1))
    dp[idx] = max_value
    return dp[idx]
                

input_string = input()
N = len(input_string)
M = int(input())
score_dict = {}
for _ in range(M):
    string,score = input().split()
    score_dict[string] = [int(score),len(string)]



dp = [-1]*(N+1)

print(dfs(0))

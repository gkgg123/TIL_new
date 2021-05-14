N = int(input())

def dfs(digit,N):
    if digit == -1:
        return
    else:
        for i in range(10):
            if N <= dp[digit][i]:
                print(i,end='')
                dfs(digit-1,N)
                break
            else:
                N -= dp[digit][i]


def find_len(N):
    digit = -1
    for i in range(10):
        line_sum = sum(dp[i])
        if N <= line_sum:
            digit = i
            break
        else:
            N -= line_sum
    
    if digit == -1:
        print(-1)
    else:
        dfs(i,N)


dp = [[0]*10 if i!=0 else [1]*10 for i in range(10)]

for i in range(1,10):
    for k in range(i,10):
        dp[i][k] = sum(dp[i-1][:k])

find_len(N+1)

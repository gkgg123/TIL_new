import sys
def input():
    return sys.stdin.readline().rstrip()
N = int(input())
def solve(bit):
    temp = 0
    for row in range(N):
        t_cnt = 0
        for col in range(N):
            if bit & ( 1<< col):
                if arr[row][col] == 'H':
                    t_cnt += 1
            elif arr[row][col] == 'T':
                t_cnt += 1
        if t_cnt < (N-t_cnt):
            temp += t_cnt
        else:
            temp += (N-t_cnt)
        if temp >= answer:
            return float('inf')
    return temp
    
arr = [list(input()) for _ in range(N)]
answer = 0
dp = [[-1 -1] for _ in range(N)]
for row in range(N):
    for col in range(N):
        if arr[row][col] == 'T':
            answer += 1
for bit in range(1<<N):
    temp = solve(bit)
    if temp < answer:
        answer = temp
    if answer == 0:
        break

print(answer)
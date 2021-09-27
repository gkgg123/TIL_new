import sys

def input():
    return sys.stdin.readline().rstrip()


mod = 1000000007
N = int(input())
arr = list(map(int,input().split()))
arr.sort()

power_value = [1]

for _ in range(N-1):
    power_value.append(power_value[-1]*2%mod)

answer = 0
for i in range(N):
    answer = (answer + (power_value[i] - power_value[N-i-1])*arr[i])%mod
print(answer)
import sys
import math
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
numbers = [int(input()) for _ in range(N)]
K = int(input())
calcurate_maps = [[ (canBeNumber*(10 ** len(str(numbers[ind]))) + numbers[ind]) % K      for canBeNumber in range(K)] for ind in range(N)]
dp = [[0 for _ in range(K)] for _ in range(1<<N)] 
dp[0][0] = 1
total_bit = (1<<N)-1
for bit in range(1<<N):
    for ind in range(N):
        if bit&(1<<ind):continue
        for mod in range(K):
            if dp[bit][mod]:
                dp[bit|(1<<ind)][calcurate_maps[ind][mod]] += dp[bit][mod]
answer = dp[total_bit][0]
total = sum(dp[total_bit])
_gcd = math.gcd(answer,total)
print(f'{answer//_gcd}/{total//_gcd}')
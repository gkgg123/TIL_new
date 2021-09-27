import sys

def input():
    return sys.stdin.readline().rstrip()
def power_divide_conquest(val,power_number):
    res = 1
    val %= mod
    while power_number:
        if power_number%2:
            res = res*val%mod
        val = val*val%mod
        power_number//=2
    return res

N = int(input())

arr = list(map(int,input().split()))
arr.sort()
mod = 1000000007

answer = 0

for i in range(N):
    answer = (answer + (power_divide_conquest(2,i) - power_divide_conquest(2,N-i-1))*arr[i])%mod

print(answer)
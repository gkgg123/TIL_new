import sys

def input():
    return sys.stdin.readline().rstrip()
def power_divide_conquest(val,power_number):
    result = 1
    val = val%mod
    while power_number > 0:
        if power_number%2:
            result = result*val%mod
        val = val*val%mod
        power_number //=2
    return result
    

max_number = 4000000
M = int(input())
mod = 1000000007
factorial = [0]*(max_number+1)
inverse = [0]*(max_number+1)
inverse[0] = 1
inverse[1] = 1
factorial[1] = 1
for i in range(2,max_number+1):
    factorial[i] = (factorial[i-1]*i)%mod
    inverse[i] = mod - (mod//i) * inverse[mod%i]%mod
for i in range(2,max_number+1):
    inverse[i] = (inverse[i]*inverse[i-1])%mod
for _ in range(M):
    N,K = map(int,input().split())
    result = (factorial[N]*inverse[N-K])%mod
    result = (result*inverse[K])%mod
    print(result)

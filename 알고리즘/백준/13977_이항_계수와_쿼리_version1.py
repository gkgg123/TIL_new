import sys

def input():
    return sys.stdin.readline().rstrip()
# a^16 =>a^2(8)
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
factorial[1] = 1
for i in range(2,max_number+1):
    factorial[i] = (factorial[i-1]*i)%mod
inverse[max_number] = power_divide_conquest(factorial[max_number],mod-2)
for i in range(max_number-1,-1,-1):
    inverse[i] = (inverse[i+1]*(i+1))%mod
print(inverse[:10])
for _ in range(M):
    N,K = map(int,input().split())
    result = (factorial[N]*inverse[N-K])%mod
    result = (result*inverse[K])%mod
    print(result)

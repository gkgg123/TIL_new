N = int(input())

prev = 1
result = 3
mod = 9901
for _ in range(N-1):
    temp = result
    result = (result*2 + prev)%mod
    prev = temp
print(result)
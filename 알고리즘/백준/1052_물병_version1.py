N,K = map(int,input().split())
result = 0
while bin(N).count('1')>K:
    t = (N&-N)
    N += t
    result += t
print(result)
    
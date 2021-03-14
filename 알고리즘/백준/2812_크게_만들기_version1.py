N,K = map(int,input().split())

number =list(input())


result = [number[0]]
idx = 1
while K and idx <N:
    while result and K and number[idx] > result[-1]:
        result.pop()
        K -= 1
    result.append(number[idx])
    idx += 1
for _ in range(K):
    result.pop()
result = result + number[idx:]
print(''.join(result))
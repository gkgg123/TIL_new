N,M = map(int,input().split())

hear = {}
for _ in range(N):
    hear[input()] = 1

result = []
for _ in range(M):
    see = input()
    if hear.get(see):
        result.append(see)

result.sort()

print(len(result))

print('\n'.join(result))
def diffcheck(A,B):
    ss = set()
    ss.update(A)
    ss.update(B)
    if len(ss) == 4:
        return True
    return False
def getDiffHeight(A,B):
    elsa = arr[A[0]] + arr[A[1]]
    anna = arr[B[0]] + arr[B[1]]
    return abs(elsa-anna)
N = int(input())

arr = list(map(int,input().split()))

arr.sort()

stack = []

for i in range(N-1):
    for j in range(i+1,N):
        stack.append((i,j))

stack.sort(key=lambda x : arr[x[0]]+arr[x[1]])
result = float('inf')
for i in range(len(stack)-1):
    if diffcheck(stack[i],stack[i+1]):
        result = min(result,getDiffHeight(stack[i],stack[i+1]))


print(result)
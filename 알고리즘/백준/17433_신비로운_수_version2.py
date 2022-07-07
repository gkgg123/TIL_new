import sys
def input():
    return sys.stdin.readline().rstrip()
def gcd(a,b):
    if a<b:
        a,b = b,a
    while b:
        a,b = b, a%b
    return a

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    gaps = []
    for idx in range(N-1):
        if arr[idx+1] - arr[idx]:
            gaps.append(arr[idx+1]-arr[idx])

    if not gaps:
        print('INFINITY')
    else:
        answer = gaps[0]
        for num in gaps:
            answer = gcd(answer,num)
        print(answer)


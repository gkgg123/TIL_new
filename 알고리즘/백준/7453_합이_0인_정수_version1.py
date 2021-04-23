import sys

input = sys.stdin.readline

N = int(input())
A= []
B = []
C = []
D = []
for _ in range(N):
    a,b,c,d = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
part_one = {}
for a in A:
    for b in B:
        if part_one.get(a+b):
            part_one[a+b] += 1
        else:
            part_one[a+b] = 1
answer = 0
for c in C:
    for d in D:
        temp_sum = -(c+d)
        if part_one.get(temp_sum):
            answer += part_one[temp_sum]



print(answer)

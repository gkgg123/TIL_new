import sys

R,C = map(int,input().split())

GR,GC,PR,PC = map(int,input().split())


arr = []
P_total = PR*PC
for _ in range(R):
    temp = list(input())
    P_total-=temp.count('P')
    arr.append(temp)

if P_total:
    print(1)
else:
    print(0)
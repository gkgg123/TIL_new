import sys

def input():
    return sys.stdin.readline().rstrip()



N = int(input())

answer = 0
temp = set()

for _ in range(N):
    s = input()
    if s == 'ENTER':
        answer += len(temp)
        temp = set()
    else:
        temp.add(s)
answer += len(temp)
print(answer)
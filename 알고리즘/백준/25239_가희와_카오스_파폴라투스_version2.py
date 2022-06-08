import sys
def input():
    return sys.stdin.readline().rstrip()

hh,mm = map(int,input().split(':'))
st = hh*60+mm
area = list(map(int,input().split()))
visited = [0 for _ in range(6)]
L = int(input())
for _ in range(L):
    x,command = input().split()
    if command == '^':
        visited[st//120] = 1
    elif 'HOUR' in command:
        t = int(command[:1])*60
        st += t
    else:
        t = int(command[:2])
        st += t
    st %= 720
    if sum(visited) == 6:
        break
ans = 0
for ind in range(6):
    if visited[ind]:
        continue
    ans += area[ind]
print(100 if ans>=100 else ans)
import sys

def input():
    return sys.stdin.readline().rstrip()

sys.setrecursionlimit(10000)
def dfs(idx,pick,N):
    if idx == N:
        if not pick:
            return
        temp = ''
        temp_set = set(pick)
        for i in range(len(st)):
            if i in temp_set:
                continue
            temp += st[i]
        answer.add(temp)
        return
    else:

        for i in range(idx,N):
            pick.extend(total[i])
            dfs(i+1,pick,N)
            pick.pop()
            pick.pop()
        dfs(i+1,pick,N)

st = input()
total = []
open_bracket = []
answer = set()
for idx in range(len(st)):
    if st[idx] == '(':
        open_bracket.append(idx)
    elif st[idx] == ')':
        prev = open_bracket.pop()
        total.append([prev,idx])



dfs(0,[],len(total))
answer = list(answer)
answer.sort()
print('\n'.join(answer))
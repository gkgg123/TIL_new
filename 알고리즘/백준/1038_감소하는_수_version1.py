# 1038 감소하는 수
# X의 자릿수가 가장 큰 자릿수
import collections
def dfs(N):
    deque = collections.deque()
    for i in range(1,10):
        deque.append((i,str(i)))
    while deque:
        if len(result) == N+1:
            break
        cur_num,to_num = deque.popleft()
        if cur_num != 0:
            for k in range(cur_num):
                temp = to_num + str(k)
                deque.append((k,temp))
                result.append((temp))


N = int(input())
result = []
for i in range(10):
    result.append(i)

if N >=10:
    dfs(N)
if len(result) > N:
    print(result[N])
else:
    print(-1)

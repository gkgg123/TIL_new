from functools import lru_cache
from collections import deque
@lru_cache(maxsize=50)
def fatorial(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    else:
        return N*fatorial(N-1)


N = int(input())

command,*arr = map(int,input().split())

patorial_cnt = []

for k in range(1,N+1):
    patorial_cnt.append(fatorial(k))
if command == 1:
    k = arr[0] - 1
    numbers = list(range(1,N+1))
    result = []
    lens = N-2
    while lens >= 0:
        copy_k = k
        ind = copy_k//patorial_cnt[lens]
        k = copy_k%patorial_cnt[lens]
        result.append(numbers.pop(ind))
        lens -= 1
    result.append(numbers.pop())
    print(*result)
else:
    numbers = list(range(1,N+1))
    result = 1
    lens = N - 2
    while arr:
        find_num = arr.pop(0)
        index = numbers.index(find_num)
        result += patorial_cnt[lens]*index
        numbers.pop(index)
        lens -= 1
    print(result)



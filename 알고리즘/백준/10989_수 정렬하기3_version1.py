# 출력을 할때에도 여러번 반복하는 것이면 곱해서 하자 곱하기가 된다.


import sys
N = int(sys.stdin.readline())
array = [0 for _ in range(10001)]
for _ in range(N):
    num = int(sys.stdin.readline())
    array[num] += 1
for k in range(10001):
    print(f'{k}\n'*array[k],end='')
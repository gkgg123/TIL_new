import sys

N = int(sys.stdin.readline())
array = [0]* 2000001
for _ in range(N):
    num = int(sys.stdin.readline())
    num += 1000000
    array[num] += 1

for num in range(2000001):
    print(f'{num-1000000}\n'*array[num],end='')
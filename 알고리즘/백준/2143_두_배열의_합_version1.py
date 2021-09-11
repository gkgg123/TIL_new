import sys
from collections import defaultdict
def input():
    return sys.stdin.readline().rstrip()

T = int(input())

N = int(input())
A_arr = [0] + list(map(int,input().split()))

M = int(input())
B_arr = [0] +list(map(int,input().split()))


for i in range(N):
    A_arr[i+1] += A_arr[i]

for j in range(M):
    B_arr[j+1] += B_arr[j]

A_nums = defaultdict(int)
B_nums = defaultdict(int)
for i in range(1,N+1):
    for j in range(i):
        A_nums[A_arr[i] - A_arr[j]] += 1

for i in range(1,M+1):
    for j in range(i):
        B_nums[B_arr[i] - B_arr[j]] += 1

result = 0
for num in A_nums:
    find_num = T -num
    if B_nums.get(find_num):
        result = result + A_nums[num] * B_nums[find_num]

print(result)

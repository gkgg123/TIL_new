import sys

def input():
    return sys.stdin.readline().rstrip()


T = int(input())
input_val = [int(input()) for _ in range(T)]

max_number = max(input_val)
arr = [1 for _ in range(max_number+1)]
prefix_sum = [0 for _ in range(max_number+1)]

for num in range(2,max_number+1):
    for multi_num in range(num,max_number+1,num):
        arr[multi_num] += num

for i in range(1,max_number+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

sys.stdout.write('\n'.join(list(map(lambda x: str(prefix_sum[x]),input_val))))
import sys
from collections import defaultdict
def input():
    return sys.stdin.readline().rstrip()

def convert_time(t):
    h,m,s_list = t.split(':')
    s,ms = s_list.split('.')
    ms = int(ms)
    s = int(s)*1000
    m = 1000*60*int(m)
    h = 1000*60*60*int(h)
    return h + m + s + ms
N = int(input())

arr = defaultdict(int)
for _ in range(N):
    start_time, end_time = input().split()
    arr[convert_time(start_time)] += 1
    arr[convert_time(end_time)] -= 1

arr_keys = sorted(arr.keys())

answer = 0
cnt = 0

for key in arr_keys:
    cnt += arr[key]
    answer = max(answer,cnt)
print(answer)
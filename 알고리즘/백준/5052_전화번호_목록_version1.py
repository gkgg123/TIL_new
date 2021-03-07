import sys

input = sys.stdin.readline

T = int(input())
def check(arr):
    for ind in range(len(arr)-1):
        if arr[ind+1].startswith(arr[ind]):
            return 'NO'
    return 'YES'



for _ in range(T):
    N = int(input())
    phone_list = [input().strip() for _ in range(N)]
    phone_list.sort()
    print(check(phone_list))
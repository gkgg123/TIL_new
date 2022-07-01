import sys

def input():
    return sys.stdin.readline().rstrip()


N,K = map(int,input().split())

arr = list(map(int,input().split()))

result = 0
left = 0
right = 0
break_point = 0
cnt = 0
while right<N:
    if not arr[right]%2:
        cnt += 1
    else:
        while break_point>=K:
            if not arr[left]%2:
                cnt -= 1
            else:
                break_point -= 1
            left += 1
        break_point += 1
    right += 1
    result = max(result,cnt)
print(result)




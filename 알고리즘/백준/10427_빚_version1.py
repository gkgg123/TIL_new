import sys

def input():
    return sys.stdin.readline().rstrip()


T = int(input())

for _ in range(T):
    N,*numbers = list(map(int,input().split()))

    numbers.sort()
    numbers = [0] + numbers
    prefix_sum = numbers[:]

    for i in range(1,N+1):
        prefix_sum[i] += prefix_sum[i-1]
    result = 0
    for gap in range(2,N+1):
        min_val = float('inf')

        for ed in range(gap,N+1):
            total_sum = prefix_sum[ed] - prefix_sum[ed-gap]
            send_money = numbers[ed]*gap - total_sum
            if send_money < min_val:
                min_val = send_money
        result += min_val
    print(result)
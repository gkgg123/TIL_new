import sys
def input():
    return sys.stdin.readline().rstrip()

def solution():
    left_Counter = [0]*60001
    right_Counter = [0]*60001
    for ind in range(1,N):
        right_Counter[arr[ind]] += 1

    answer = 0

    left_Counter[arr[0]] += 1
    for cur_ind in range(1,N-1):
        right_Counter[arr[cur_ind]] -= 1
        mid_value = arr[cur_ind]
        find_value = mid_value*2

        for left_key in range(1,find_value+1):
            if 0<find_value - left_key <=30000:
                answer = answer + left_Counter[left_key] * right_Counter[find_value-left_key]
        left_Counter[mid_value] += 1
    return answer

N = int(input())

arr = list(map(int,input().split()))




print(solution())

import sys

def input():
    return sys.stdin.readline().rstrip()


input_string = input()
N = len(input_string)
left_RK = []
right_RK = []
cnt = 0
for i in range(N):
    if input_string[i] == 'K':
        cnt += 1
    else:
        left_RK.append(cnt)
cnt = 0

for i in range(N-1,-1,-1):
    if input_string[i] == 'K':
        cnt += 1
    else:
        right_RK.append(cnt)

right_RK.reverse()


left_index = 0
right_index = len(left_RK)-1
answer = 0
while left_index<=right_index:
    answer = max(answer, right_index - left_index+1 + 2*min(left_RK[left_index],right_RK[right_index]))

    if left_RK[left_index] > right_RK[right_index]:
        right_index -= 1
    else:
        left_index += 1
print(answer)

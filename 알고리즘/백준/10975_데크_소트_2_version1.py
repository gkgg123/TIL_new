import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())
visit = [False for _ in range(N+1)]
nums = []
for idx in range(N):
    num = int(input())
    nums.append(num)

orderd_dict = {}
for idx,num in enumerate(sorted(nums)):
    orderd_dict[num] = idx

answer = 0
for num in nums:
    idx = orderd_dict[num]
    if not visit[idx]:
        answer += 1

    if idx>0:
        visit[idx-1] = True
    if idx+1<N:
        visit[idx+1] = True
    visit[idx] = True

print(answer)
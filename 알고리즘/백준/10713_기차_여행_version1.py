import sys
def input():
    return sys.stdin.readline().rstrip()


N,M = map(int,input().split())

p_list = list(map(int,input().split()))

# 구매, ic, ic구입비

basic_list = [0]
ic_list = [0]
ic_chip_list = [0]
for _ in range(N-1):
    basic,ic, ic_chip = map(int,input().split())
    basic_list.append(basic)
    ic_list.append(ic)
    ic_chip_list.append(ic_chip)


prefix_sum = [0 for _ in range(N+1)]
for ind in range(M-1):
    current_city, next_city = p_list[ind] , p_list[ind+1]
    if next_city < current_city:
        next_city,current_city = current_city, next_city

    prefix_sum[next_city] -= 1
    prefix_sum[current_city] += 1

for i in range(1,N+1):
    prefix_sum[i] += prefix_sum[i-1]


result = 0

for i in range(1,N):
    basic = basic_list[i] * prefix_sum[i]
    ic = ic_list[i] * prefix_sum[i] + ic_chip_list[i]

    result = result + min(basic,ic)
print(result)
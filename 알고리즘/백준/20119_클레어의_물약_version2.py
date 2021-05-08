import sys

input = sys.stdin.readline

N,M = map(int,input().split())
recipe_remain_cnt = []
liquid_number = []
next_recipe_array = [[] for _ in range(N+1)]
for i in range(M):
    k,*recipe,r = map(int,input().split())

    recipe_remain_cnt.append(k)
    liquid_number.append(r)

    for num in recipe:
        next_recipe_array[num].append(i)


L = int(input())
own_liquid = list(map(int,input().split()))
result = set(own_liquid)


while own_liquid:
    cur_num  = own_liquid.pop()
    for recipe_idx in next_recipe_array[cur_num]:
        recipe_remain_cnt[recipe_idx] -= 1
        if recipe_remain_cnt[recipe_idx] == 0 and liquid_number[recipe_idx] not in result:
            own_liquid.append(liquid_number[recipe_idx])
            result.add(liquid_number[recipe_idx])

print(len(result))
result = sorted(list(result))

print(*result)
import sys
from collections import defaultdict,deque
def input():
    return sys.stdin.readline().rstrip()
N,M = map(int,input().split())
material_dict = {'-1':True}
# dict를 고정시키는게 문제
material_pay = [float('inf') for _ in range(10000)]
queue = deque()
for k in range(N):
    name,pay = input().split()
    material_dict[name] = k+1
    material_pay[k+1] = int(pay)
    queue.append(material_dict[name])



graph = defaultdict(list)


total_recipe_list = [input() for _ in range(M)]
recipe_cnt = defaultdict(int)
recipe_dict = defaultdict(list)
recipe_order = defaultdict(list)
total_recipe_list.sort()

for total_recipe in total_recipe_list:
    complete_name,arg = total_recipe.split('=')
    recipe = arg.split('+')
    if material_dict.get(complete_name):
        complete_idx = material_dict[complete_name]
    else:
        complete_idx = len(material_dict.keys())
        material_dict[complete_name] = complete_idx

    recipe_idx = (complete_idx,recipe_cnt[complete_idx])
    recipe_cnt[complete_idx] += 1
    temp_set = set()
    temp = defaultdict(int)
    for res in recipe:
        cnt,name = int(res[0]),res[1:]
        if material_dict.get(name):
            name_idx = material_dict[name]
        else:
            name_idx = len(material_dict.keys())
            material_dict[name] = name_idx
        if recipe_idx not in graph[name_idx]:
            graph[name_idx].append(recipe_idx)
        temp_set.add(name_idx)
        temp[name_idx] += cnt
    recipe_order[complete_idx].append(temp_set)
    recipe_dict[complete_idx].append(temp)

flag = True
        
total_len = len(material_dict) - 1
cnt = 0
while queue:

    name_idx = queue.popleft()
    if graph.get(name_idx):
        for next_idx,recipe_idx in graph[name_idx]:
            # 다시 들어왔을때 문제
            if name_idx in recipe_order[next_idx][recipe_idx]:
                recipe_order[next_idx][recipe_idx].remove(name_idx)


            if not len(recipe_order[next_idx][recipe_idx]):
                temp = 0

                for mat,val in recipe_dict[next_idx][recipe_idx].items():
                    temp += material_pay[mat]*val
                if material_pay[next_idx] > temp:

                    queue.append(next_idx)
                    material_pay[next_idx] = temp
                
if material_dict.get('LOVE'):
    result = material_pay[material_dict['LOVE']]
    if result == float('inf'):
        print(-1)
    elif result > 1000000000:
        print(1000000001)
    else:
        print(result)
else:
    print(-1)
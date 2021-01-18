# 18231 파괴된 도시






N,M = map(int,input().split())

graph = {i:[] for i in range(N+1)}

for _ in range(M):
    node1,node2 = map(int,input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

destory_cnt = int(input())
destroy_citys = list(map(int,input().split()))
result = []
destroyed = []
for destroy_city in destroy_citys:
    temp = [destroy_city]
    for city in graph[destroy_city]:
        if city not in destroy_citys:
            break
        else:
            temp.append(city)
    else:
        result.append(destroy_city)
        destroyed.extend(temp)
    if len(set(destroyed)) == destory_cnt:
        print(len(result))
        result.sort()
        print(' '.join(list(map(str,result))))
        break
else:
    print(-1)
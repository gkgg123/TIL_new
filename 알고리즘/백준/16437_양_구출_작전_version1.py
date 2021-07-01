import sys
sys.setrecursionlimit(123456)
def dfs(node):
    if not graph[node]:
        if pet_list[node]>0:
            return pet_list[node]
        return 0 
    else:
        temp = 0
        for child_node in graph[node]:
            temp += dfs(child_node)
        temp += pet_list[node]
        if temp <0:
            temp = 0
        return temp

def input():
    return sys.stdin.readline().rstrip()
N = int(input())

graph = [[] for _ in range(N+1)]
pet_list = [0 for _ in range(N+1)]
for i in range(2,N+1):
    pet,*arg = input().split()
    pay,island = map(int,arg)
    if pet == 'S':
        pet_list[i] = pay
        graph[island].append(i)
    else:
        pet_list[i] = -pay
        graph[island].append(i)




print(dfs(1))
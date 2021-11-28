import sys
def input():
    return sys.stdin.readline().rstrip()

N,M = map(int,input().split())

dict_list =  {}


for _ in range(N):
    s = input()
    dict_list[s] = dict_list.get(s,0) + 1
K = int(input())
result = 0
for key in dict_list:
    if result > dict_list[key]:
        continue
    count = key.count('0')
    if count <= K and not (K-count)%2:
        result = max(result,dict_list[key])
print(result)
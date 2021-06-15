import sys
input = sys.stdin.readline
def get_prim_number(input_Num):
    last_num = input_Num
    visited = [False for _ in range(last_num+1)]
    visited[0] = True
    visited[1] = True

    result = []
    for num in range(2,last_num+1):
        if not visited[num]:
            result.append(num)
            for new_num in range(2*num,last_num+1,num):
                visited[new_num] = True
    return result
N = int(input())

arr = list(map(int,input().split()))
result = []
max_num = max(arr)
prim_set = get_prim_number(max_num)
for val in arr:
    if val in prim_set:
        result.append(val)

if len(result)>0:
    answer = 1
    result = set(result)
    for prim in result:
        answer*=prim
    print(answer)
else:
    print(-1)
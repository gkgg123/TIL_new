
import sys

input = sys.stdin.readline

T = int(input())

def find_parents(node):
    parent_list = [node]

    while parent_num[node] != -1:
        parent = parent_num[node]
        parent_list.append(parent)
        node = parent

    return parent_list



for _ in range(T):
    N = int(input())
    parent_num = [-1]*(N+1) # 해당 index의 부모가 안에 들어가 있다.
    for _ in range(N-1):
        parent,child = map(int,input().split())
        parent_num[child] = parent


    num1,num2 = map(int,input().split())

    parents1 = find_parents(num1)
    parents2 = find_parents(num2)

    if len(parents1) < len(parents2):
        parents1,parents2 = parents2, parents1
    result = -1
    for num in parents1:
        if num in parents2:
            result = num
            break
    print(result)
import heapq
import sys

def input():
    return sys.stdin.readline().rstrip()
Q = int(input())

gorilla_list = {}
result = 0
for _ in range(Q):
    command,name,k,*arg = input().split()
    k = int(k)
    if arg:
        arg = list(map(int,arg))
        arg.sort()
        gorilla_list[name] = list(heapq.merge(gorilla_list.get(name,[]),arg))
    else:
        if gorilla_list.get(name,[]):
            if len(gorilla_list[name])<k:
                temp = sum(gorilla_list[name])
                gorilla_list[name] = []
                result += temp
            else:
                for _ in range(k):
                    result += gorilla_list[name].pop()

print(result)
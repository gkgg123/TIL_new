import heapq
import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()
Q = int(input())

gorilla_list = {}
result = 0
for _ in range(Q):
    input_list = input().split()
    command = int(input_list[0])
    name = input_list[1]
    k = int(input_list[2])
    if command == 1:
        arg = list(map(int,input_list[3:]))
        if not gorilla_list.get(name):
            gorilla_list[name] = []
        for row in arg:
            heapq.heappush(gorilla_list[name],-row)
    else:
        if gorilla_list.get(name):
            if len(gorilla_list[name])<k:
                result = result + -sum(gorilla_list[name])
                gorilla_list[name] = []
            else:
                for _ in range(k):
                    result -= heapq.heappop(gorilla_list[name])
print(result)
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
def solve(A,B,C): 

    visited = set()
    if (A+B+C)%3:
        return 0
    else:
        sorted_list = tuple(sorted([A,B,C]))
        visited.add(sorted_list)
        
        que = deque()
        que.append(sorted_list)
        while que:
            A,B,C = que.popleft()
            if A == B == C:
                return 1
            
            new_A = 2*A; new_B = B-A; new_C = C-A
            sorted_A = tuple(sorted([new_A,new_B,C]))
            if sorted_A not in visited:
                que.append(sorted_A)
                visited.add(sorted_A)
            sorted_B = tuple(sorted([new_A,B,new_C]))
            if sorted_B not in visited:
                que.append(sorted_B)
                visited.add(sorted_B)
        return 0 


A,B,C = map(int,input().split())
print(solve(A,B,C))
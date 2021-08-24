import sys
sys.setrecursionlimit(1000005)
def input():
    return sys.stdin.readline().rstrip()

def cycle_check(idx):
    if visited[idx]:
        return
    visited[idx] = True
    cycle_list.append(idx)
    cycle_check(D[idx])
    
N, K = map(int,input().split())
cards = [0]+list(map(int,input().split()))
D = [0]+list(map(int,input().split()))

result = [0 for _ in range(N+1)]
visited = [False for _ in range(N+1)]


for idx in range(1,N+1):
    if not visited[idx]:
        cycle_list = []
        cycle_check(idx)
        cycle_len = len(cycle_list)
        for cycle_idx,cycle_val in enumerate(cycle_list):
            result_idx = cycle_list[(cycle_idx + K%cycle_len)%cycle_len]
            result[result_idx] = cards[cycle_val]


print(*result[1:])
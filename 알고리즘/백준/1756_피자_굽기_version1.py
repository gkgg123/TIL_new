import sys

def input():
    return sys.stdin.readline().rstrip()

H,N = map(int,input().split())

heights = [float('inf')] + list(map(int,input().split()))

for idx in range(1,H+1):
    if heights[idx] > heights[idx-1]:
        heights[idx] = heights[idx-1]

pizzas = list(map(int,input().split()))

pizza_idx = 0
result = 0
for idx in range(H,0,-1):
    if heights[idx] >= pizzas[pizza_idx]:
        pizza_idx += 1
        result = idx
    if pizza_idx == N:
        break

if pizza_idx == N:
    print(result)
else:
    print(0)
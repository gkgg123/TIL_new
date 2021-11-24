import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())

crane = list(map(int,input().split()))
crane.sort(reverse=True)
M = int(input())

box = list(map(int,input().split()))
box.sort(reverse=True)
if box[0]> crane[0]:
    print(-1)
else:
    times = 0
    cnt = 0
    next_position = [0 for _ in range(N)]
    while True:
        if cnt == M:
            break
        for c in range(N):
            for k in range(next_position[c],len(box)):
                if crane[c] >= box[k]:
                    next_position[c] = k+1
                    box[k] = float('inf')
                    cnt += 1
                    break
                else:
                    next_position[c] = k+1
        times += 1
    print(times)
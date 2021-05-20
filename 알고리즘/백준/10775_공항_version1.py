import sys
input = sys.stdin.readline


G = int(input())
P = int(input())
result = 0
plane = [int(input()) for _ in range(P)]


parents_number = [i for i in range(G+1)]

visited = [False]*(G+1)
cur_idx = 0
planing = True

while cur_idx<P and planing:

    cur_plane_number = plane[cur_idx]
    check = [cur_plane_number]
    while visited[cur_plane_number] and cur_plane_number>0:
        cur_plane_number = parents_number[cur_plane_number]
        check.append(cur_plane_number)
    
    
    
    if cur_plane_number == 0:
        break
    else:
        visited[cur_plane_number] = True
        for num in check:
            parents_number[num] = cur_plane_number-1

    cur_idx += 1

print(cur_idx)


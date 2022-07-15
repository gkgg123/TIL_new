import sys

def input():
	return sys.stdin.readline().rstrip()
	
N,M = map(int,input().split())



arr = [list(map(int,input().split())) for _ in range(N)]

dx = [1,0,-1,1,-1,1,0,-1]
dy = [-1,-1,-1,0,0,1,1,1]


visited = [[False for _ in range(M)] for _ in range(N)]

cnt = 0
for x in range(N):
	for y in range(M):
		if visited[x][y]:
			continue
		if not arr[x][y]:
			continue
		queue = [(x,y)]
		visited[x][y] = True
		flag = True
		while queue:
			cx,cy = queue.pop()
			for i in range(8):
				nx = cx + dx[i]
				ny = cy + dy[i]
				if 0<=nx<N and 0<=ny<M:
					if arr[nx][ny]>arr[x][y]:
						flag = False
						continue
					if visited[nx][ny]:
						continue
					if arr[nx][ny] == arr[x][y]:
						visited[nx][ny] = True
						queue.append((nx,ny))
		if flag:
			cnt += 1
print(cnt)
					
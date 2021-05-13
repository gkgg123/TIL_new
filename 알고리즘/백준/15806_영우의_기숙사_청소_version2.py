import sys
from collections import deque

def grow(arr,queue):
    dx = [-2,-1,1,2,2,1,-1,-2]
    dy = [-1,-2,-2,-1,1,2,2,1]

    while queue:
        x,y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <=nx<N and 0<=ny<N:
                if arr[nx][ny] == -1:
                    arr[nx][ny] = arr[x][y] + 1
                    queue.append((nx,ny))


input = sys.stdin.readline


N,M,K,T = map(int,input().split())
mold_even = deque()
mold_odd = deque()
odd_list =[[-1]*N for _ in range(N)]
even_list = [[-1]*N for _ in range(N)]
for i in range(M):
    x,y = map(lambda x: x-1,map(int,input().split()))
    if (x+y)%2:
        odd_list[x][y] = 0
        mold_odd.append((x,y))
    else:
        even_list[x][y] = 0
        mold_even.append((x,y))



grow(even_list,mold_even)
grow(odd_list,mold_odd)
# 초기값이 홀수이면 odd에 있는데 이 경우, T가 짝수일때에만 ON이 된상태이다.
# odd_list : odd이면 T가 짝수이면 ON
# odd_list : odd이면 T가 홀수이면 off
# even_list : odd이면서 T가 짝수이면 off
# even_list : odd이면서 T가 홀수이면 ON
# 이렇게 되기 때문에 odd이면서 T가 짝수이면 odd_list를 odd이면서 T가 홀수이면 even_list를 탐색해줘야한다.
# even도 똑같이 해주면 된다.
for _ in range(K):
    x,y = map(lambda x: x-1,map(int,input().split()))
    flag = True
    if (x+y)%2 and T%2:
        flag = False
    elif (x+y)%2 == 0 and T%2==0:
        flag = False
    if flag and 0<=odd_list[x][y]<=T:
        print('YES')
        break
    elif not flag and 0<=even_list[x][y]<=T:
        print('YES')
        break
else:
    print('NO')

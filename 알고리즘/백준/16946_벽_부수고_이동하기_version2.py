# 16946 벽 부수고 이동하기 4

# dfs를 해준다. 여기서 일반적인 dfs와 다른점은 방문표시 대신 해당 위치의 값을 들어온 index값으로 변형시켜준다.
def dfs(x,y,index):
    global index_dict,N,M

    stack = [(x,y)]
    cnt = 1
    arr[x][y] = index
    while stack:
        cx,cy = stack.pop()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if not arr[nx][ny]:
                    stack.append((nx,ny))
                    arr[nx][ny] = index
                    cnt += 1
    # dfs를 전부 한뒤에 그 개수를 딕셔너리에 저장해준다.
    index_dict[index] = cnt




# dfs를 이용해서 쉽게 풀수 있었던 문제


N,M = map(int,input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]
arr = [list(map(int,list(input()))) for _ in range(N)]
# 원본이 저장된 arr
result = [['0']*M for _ in range(N)]
# 결과값들을 저장해놓는 result 배열을 만들어둔다.

# 빈칸인 개수를 세주기 위해서 초기값을 -1로 해줬다. 왜냐하면 arr에는 1,0이 있으므로 겹쳐지지 않게 -1부터 시작해서 1씩 작아지게 해줬다.
# 그리고 해당 인덱스에 연결된 개수를 저장하기 위한 index_dict라는 딕셔너리를 미리 만들어줬다.
index = -1
index_dict = {}

# 빈칸의 개수를 세어주기 위한 dfs 공정
for x in range(N):
    for y in range(M):
        if not arr[x][y]:
            dfs(x,y,index)
            index -= 1

for x in range(N):
    for y in range(M):
        if arr[x][y] == 1:
            # 원본 배열에서 벽이 있을때, 그 벽 주변의 상황을 파악하고, 그 중에 1이 아닌 우리가 설정한 index값을 집합에 저장해준다.
            temp = set()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<N and 0<=ny<M:
                    if arr[nx][ny] != 1:
                        temp.add(arr[nx][ny])
            # 기본값은 1이고, temp에 저장된 index들을 반복문을 돌려 움직일수 있는 칸의 개수를 세준다.
            move_wall = 1
            for index in temp:
                move_wall += index_dict[index]
            # 그리고 result에 10으로 나눈 나머지를 string형태로 저장해준다.
            result[x][y] = str(move_wall%10)
# join을 이용해 출력해준다.
for row in result:
    print(''.join(row))
# heecheol1508 클론코딩


R,C,N = map(int,input().split())
board = [list(input()) for _ in range(R)]

if N%2 == 0:
    # 시간이 짝수일때는 무조건 전부 폭탄이 설치되기 때문에, 시간이 짝수일때는 전부 폭탄이 설치된 경우를 출력하면 된다.
    for _ in range(R):
        print('O'*C)
elif N == 1:
    # 1초일때는 초기 상태를 그대로 출력하면 된다.
    for row in board:
        print(''.join(row))
else:
    # 그 외의 시간일때는 나머지를 출력하면 된다.
    # 그런데 해당문제에서는 폭탄이 터지는 경우는 크게 2가지 밖에 없다.
    # 최초 설치된 폭탄 즉 0초에 설치된 폭탄이 터지는 경우와 
    # 2초에 설치된 폭탄 중에 최초 설치된 폭탄과 인접하지 않는 폭탄이 터지는 경우 2가지밖에 없다.
    # 그렇기 때문에 최초 설치된 폭탄이 터ㅣ는 시간대와 2초에 설치된 폭탄이 터지는 경우 두가지만 구분하면 된다.
    # 최초 설치된 폭탄이 터지는 시간대는 3초,7초,11초,15초로 4초 간격으로 터진다. 
    # 2초에 설치된 폭탄 중 최초 설치된 폭탄과 인접하지 않은 폭탄이 터지는 시간은 5초,9초,13초,17초이다.
    # 먼저 터지는 것은 최초 설치된 폭탄의 위치와 그와 인접한 폭탄이다. 그 부분만 폭탄이 터지는걸로 해주고 나머지는 폭탄이 설치된 걸로 만들어주면 된다.
    # 그래서 최초 폭탄이 터졌을때의 상황을 만들어주고, 그때의 시간이 3,7,11,15일때에는 그대로 출력하고,
    # 그때가 아닐때에는 2초에 설치된 폭탄이 터지는 경우이니 한번 더 폭탄이 터지는 것을 반복해주면 된다.
    bomb = []
    for x in range(R):
        for y in range(C):
            if board[x][y] == 'O':
                board[x][y] = '.'
                bomb.append((x,y))
            else:
                board[x][y] = 'O'
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for bx,by in bomb:
        for i in range(4):
            nx = bx + dx[i]
            ny = by + dy[i]
            if 0<=nx<R and 0<=ny<C:
                board[nx][ny] = '.'

    times = (N-3)%4
    if not times:
        for row in board:
            print(''.join(row))
    else:
        bomb = []
        for x in range(R):
            for y in range(C):
                if board[x][y] == 'O':
                    bomb.append((x,y))
                    board[x][y] = '.'
                else:
                    board[x][y] = 'O'
        for bx,by in bomb:
            for i in range(4):
                nx = bx + dx[i]
                ny = by + dy[i]
                if 0<=nx<R and 0<=ny<C:
                    board[nx][ny] = '.'
        for row in board:
            print(''.join(row))
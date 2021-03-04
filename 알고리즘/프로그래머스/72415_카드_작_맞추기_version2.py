from collections import deque
import functools
def solution(board,r,c):
    card_dict = [[] for i in range(7)]
    card_tuple = set() 
    for x in range(4):
        for y in range(4):
            if board[x][y]:
                card_dict[board[x][y]].append((x,y))
                card_tuple.add(board[x][y])
    card_tuple = tuple(card_tuple)
        
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    def outOfrange(x,y):
        if 0 > x or x >3 or y<0 or y>3:
            return True
        return False
        
    @functools.lru_cache(maxsize=None)
    def bfs(s,t,cards):
        if s == t:
            return 0
        stack = deque()
        stack.append((s[0],s[1],0))
        visited = set()
        while stack:
            x,y,cnt = stack.popleft()
            for i in range(4):
                repeat = 0
                while True:
                    nx = x + dx[i]*repeat
                    ny = y + dy[i]*repeat
                    if outOfrange(nx+dx[i],ny+dy[i]) or (repeat != 0 and board[nx][ny] in cards):
                        break
                    repeat += 1
                for re in [1,repeat]:
                    nx = x + dx[i]*re
                    ny = y + dy[i]*re
                    if outOfrange(nx,ny):
                        continue
                    if (nx,ny) == t:
                        return cnt + 1
                    if (nx,ny) not in visited:
                        visited.add((nx,ny))
                        stack.append((nx,ny,cnt+1))

    @functools.lru_cache(maxsize=None)
    def find_card_short_count(cur_position,cards):
        if len(cards) == 0:
            return 0
        min_distance = float('inf')
        for pick_card in cards:
            position1,position2 = card_dict[pick_card]
            remain_cards = tuple(card for card in cards if card != pick_card)
            direction1 = bfs(cur_position,position1,cards) + bfs(position1,position2,cards) + find_card_short_count(position2,remain_cards)
            direction2 = bfs(cur_position,position2,cards) + bfs(position2,position1,cards) + find_card_short_count(position1,remain_cards)
            min_distance = min(min_distance,direction1,direction2)
        return min_distance

    answer = len(card_tuple)*2 + find_card_short_count((r,c),card_tuple)
    return answer


a = solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0)
print(a)
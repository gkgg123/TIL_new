def check(x,y,size):
    if x + size > 10 or y + size >10:
        return False
    for dx in range(size):
        for dy in range(size):
            if not arr[x+dx][y+dy]:
                return False
    return True


def set_position(x,y,size,val):
    for dx in range(size):
        for dy in range(size):
            arr[x+dx][y+dy] = val
def dfs(x,y,cnt):
    global result
    if cnt >= result:
        return
    finish = True
    while x < 10:
        while y < 10:
            if arr[x][y] == 1:
                finish = False
                for paper_size in range(5,0,-1):
                    if paper[paper_size] and check(x,y,paper_size):
                        set_position(x,y,paper_size,0)
                        paper[paper_size] -= 1
                        dfs(x,y+paper_size-1,cnt+1)
                        paper[paper_size] += 1
                        set_position(x,y,paper_size,1)
                return
            y += 1
        x += 1
        y = 0
    if finish:
        result = min(result,cnt)
        


arr = [list(map(int,input().split())) for _ in range(10)]
paper = [0]+[5]*5
result = float('inf')
dfs(0,0,0)
print(result if result != float('inf') else -1)
def dfs(x,y,cnt):
    global result
    if cnt > result:
        return
    if x >= 10:
        result = min(result,cnt)
        return
    if y >= 10:
        dfs(x+1,0,cnt)
        return
    if arr[x][y] == 1:
        for paper_size in range(5,0,-1):
            if paper[paper_size]:
                if x + paper_size <= 10 and y + paper_size <= 10:
                    flag = False
                    for dx in range(paper_size):
                        for dy in range(paper_size):
                            if not arr[x+dx][y+dy]:
                                flag = True
                                break
                        if flag:
                            break
                    if not flag:
                        for dx in range(paper_size):
                            for dy in range(paper_size):
                                arr[x+dx][y+dy] = 0
                        paper[paper_size] -= 1
                        dfs(x,y+paper_size-1,cnt+1)
                        paper[paper_size] += 1
                        for dx in range(paper_size):
                            for dy in range(paper_size):
                                arr[x+dx][y+dy] = 1
    else:
        dfs(x,y+1,cnt)

        


arr = [list(map(int,input().split())) for _ in range(10)]
paper = [0]+[5]*5
result = float('inf')
dfs(0,0,0)
print(result if result != float('inf') else -1)
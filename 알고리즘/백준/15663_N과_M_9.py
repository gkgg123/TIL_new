def dfs(cnt,goal,res):
    if cnt == goal:
        print(*res)
        return
    else:
        for i in range(N):
            if visited[i]:
                temp = res + [arr[i]]
                if tuple(temp) not in record:
                    visited[i] = False
                    record.add(tuple(temp))
                    dfs(cnt+1,goal,temp)
                    visited[i] = True


N,M = map(int,input().split())
visited = [True]*N
record = set()
arr = list(map(int,input().split()))

arr.sort()


dfs(0,M,[])
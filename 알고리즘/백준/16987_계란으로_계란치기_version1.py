import sys

def input():
    return sys.stdin.readline().rstrip()
def dfs(ind,pajijik):
    global result
    if ind == N:
        result = max(result,pajijik)
        return
    elif (N-ind) * 2 + pajijik < result:
        return
    else:
        if eggs[ind][0]<=0:
            dfs(ind+1,pajijik)
        else:
            flag = True
            for next_ind in range(N):
                if ind == next_ind:
                    continue
                if eggs[next_ind][0]>0:
                    temp_pajijik = pajijik
                    eggs[next_ind][0] -= eggs[ind][1]
                    eggs[ind][0] -= eggs[next_ind][1]
                    if eggs[ind][0]<=0:
                        temp_pajijik += 1
                    if eggs[next_ind][0]<= 0:
                        temp_pajijik += 1
                    dfs(ind+1,temp_pajijik)
                    flag = False
                    eggs[next_ind][0] += eggs[ind][1]
                    eggs[ind][0] += eggs[next_ind][1]
            if flag:
                dfs(ind+1,pajijik)

N = int(input())

eggs = [list(map(int,input().split())) for _ in range(N)]

result = 0
dfs(0,0)
print(result)
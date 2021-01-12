import itertools
import collections

def bfs(arr,team):
    q=collections.deque()
    q.append(arr)
    cnt=1
    visited[arr]=True
    while q:
        node=q.popleft()
        for k in graph[node]:
            if visited[k]==False and k in team:
                visited[k]=True
                q.append(k)
                cnt+=1
    if cnt==len(team):
        return True
    else:
        return False
 

N=int(input())
arr=list(range(1,N+1))
people=[0]

people.extend(list(map(int,input().split())))
graph=[[]]
people_total=sum(people)
for i in range(N):
    temp=list(map(int,input().split()))
    graph.append(temp[1:])
min_number=999999999999999
for i in range(1,N//2+1):
    b=itertools.combinations(arr,i)
    for k in b:
        a_team=list(k)
        b_team=list(set(arr)-set(k))
        
        visited=[False]*(N+1)
        
        if bfs(a_team[0],a_team) and bfs(b_team[0],b_team):        
            a_team_sum=0
            for tt in a_team:
                a_team_sum+=people[tt]
            b_team_sum=people_total-a_team_sum
            if abs(b_team_sum-a_team_sum)<=min_number:
                min_number=abs(b_team_sum-a_team_sum)       
    if min_number==0:
        break
if min_number>1000:
    print(-1)
else:
    print(min_number)
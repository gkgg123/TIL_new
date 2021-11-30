import sys
input = sys.stdin.readline
n,m,r  = map(int, input().split())
data = [ list(map(int,input().split())) for _ in range(n)]
temp =[ [0 for _ in range(m)] for i in range(n)]
#회전하는 함수 
def rotate():
    for i in range(min(n,m)//2): #줄별로 회전시킴
        # 좌측 최하단의 점을 빼준다. 예제(4,1) 점을 빼주는 형식
        pick = data[n-1-i][i]
        # 우측 최하단에서부터 회전하는 방향을 역으로 한다고 생각
        # (4,1)<-(3,1)<-(2,1) 을 차례 채워준다고 생각하면 된다.  
        for j in range(n-1-i-1,i-1,-1):
            data[j+1][i] = data[j][i]                
                
        # 제일 윗줄
        for j in range(i+1,m-i):
            data[i][j-1] = data[i][j]
        # 제일 오른쪽 줄        
        for j in range(i+1,n-i):
            data[j-1][m-i-1] = data[j][m-i-1]
        # 제일 아랫줄
        for j in range(m-2-i,i,-1):
            data[n-1-i][j+1] = data[n-1-i][j]
        data[n-1-i][i+1] = pick
#r번 회전
for k in range(r):    
    rotate()
#결과 출력   

#결과 출력   
for i in data:
        for j in i:
            print(j, end=' ')
        print('')

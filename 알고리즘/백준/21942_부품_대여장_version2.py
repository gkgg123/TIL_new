from datetime import datetime,timedelta
import sys

input = sys.stdin.readline


N,L,F = input().split()
N = int(N)
F = int(F)

L = timedelta(days=int(L[:3]),hours=int(L[4:6]),minutes=int(L[7:]))


trady_dict = {}

brrow_dict = {}

for i in range(N):
    date,times,part_name,name = input().split()
    year,month,day = map(int,date.split('-'))
    hours,mins = map(int,times.split(':'))
    timestamp = datetime(year,month,day,hours,mins)
    if brrow_dict.get((part_name,name)):
        delta = timestamp - brrow_dict[(part_name,name)]
        if delta > L:
            
    else:
        brrow_dict[(part_name,name)] = timestamp